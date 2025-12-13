# streamlit_app.py
"""
Simple Streamlit UI for the RealEstate investor models.
Place your ./models folder (final_best_classifier.joblib, final_regressor_RF.joblib,
final_regressor_XGB.joblib, preprocessor.joblib, scales.json) next to this file.

Run:
    streamlit run streamlit_app.py
"""
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import json
from io import BytesIO
import matplotlib.pyplot as plt
from typing import Dict

st.set_page_config(page_title="RealEstate Investor", layout="wide", initial_sidebar_state="expanded")
st.title("🏡 Real Estate Investment Advisor")
st.markdown("Upload a CSV or enter a single property. The app will load saved models (if present) and predict.")

# -------------------------
# Paths (update if needed)
# -------------------------
MODEL_DIR = "./models"
CLF_PATH = os.path.join(MODEL_DIR, "final_best_classifier.joblib")
RF_PATH = os.path.join(MODEL_DIR, "final_regressor_RF.joblib")
XGB_PATH = os.path.join(MODEL_DIR, "final_regressor_XGB.joblib")
PREPROC_PATH = os.path.join(MODEL_DIR, "preprocessor.joblib")
SCALES_PATH = os.path.join(MODEL_DIR, "scales.json")

# -------------------------
# Load artifacts (cached)
# -------------------------
@st.cache_resource
def load_artifacts():
    artifacts = {}
    # scales
    if os.path.exists(SCALES_PATH):
        try:
            with open(SCALES_PATH, "r") as f:
                artifacts["scales"] = json.load(f)
        except Exception:
            artifacts["scales"] = {}
    else:
        artifacts["scales"] = {}

    # models & preprocessor (load safely)
    def safe_load(p):
        try:
            return joblib.load(p) if os.path.exists(p) else None
        except Exception:
            return None

    artifacts["clf"] = safe_load(CLF_PATH)
    artifacts["reg_rf"] = safe_load(RF_PATH)
    artifacts["reg_xgb"] = safe_load(XGB_PATH)
    artifacts["preprocessor"] = safe_load(PREPROC_PATH)
    return artifacts

art = load_artifacts()

# Sidebar controls
st.sidebar.header("Controls")
mode = st.sidebar.radio("Mode", ["Single property", "CSV batch predict", "Explore & Visualize"])
use_rf = st.sidebar.checkbox("Use RF regressor", value=True)
use_xgb = st.sidebar.checkbox("Use XGB regressor", value=True)
use_clf = st.sidebar.checkbox("Use classifier", value=True)
show_debug = st.sidebar.checkbox("Show engineered inputs", value=False)
if st.sidebar.button("Reload artifacts"):
    st.cache_resource.clear()
    st.experimental_rerun()

CURRENT_YEAR = pd.Timestamp.now().year

# -------------------------
# Feature engineering helper
# (keeps parity with your notebook)
# -------------------------
def build_engineered_row(raw: Dict):
    r = dict(raw)  # copy
    # defaults (same as earlier notebook)
    dd = dict(
        Price_in_Lakhs=254.0,
        Size_in_SqFt=2750,
        BHK=3,
        Year_Built=2006,
        Nearby_Schools=5,
        Nearby_Hospitals=5,
        Public_Transport_Accessibility="Medium",
        Amenities="",
        Floor_No=15,
        Total_Floors=15,
        State="missing",
        City="missing",
        Locality="missing",
        Property_Type="Apartment",
        Furnished_Status="Unfurnished",
        Parking_Space="No",
        Security="No",
        Facing="North",
        Owner_Type="Owner",
        Availability_Status="Ready_to_Move"
    )
    for k, v in dd.items():
        if k not in r or r[k] is None:
            r[k] = v

    # required conversions / safety
    price = float(r.get("Price_in_Lakhs", dd["Price_in_Lakhs"]))
    size = float(r.get("Size_in_SqFt", dd["Size_in_SqFt"]))
    bhk = int(r.get("BHK", dd["BHK"]))
    floor_no = float(r.get("Floor_No", dd["Floor_No"]) or dd["Floor_No"])
    total_floors = float(r.get("Total_Floors", dd["Total_Floors"]) or dd["Total_Floors"])
    year_built = int(r.get("Year_Built", dd["Year_Built"]))

    # engineered features (same formulas)
    ppsf = price / max(size, 1.0)
    school_score = float(r.get("Nearby_Schools", dd["Nearby_Schools"])) / 10.0
    hosp_score = float(r.get("Nearby_Hospitals", dd["Nearby_Hospitals"])) / 10.0
    tmap = {"Low": 0.3, "Medium": 0.6, "High": 1.0}
    transport_score = tmap.get(str(r.get("Public_Transport_Accessibility", "Medium")), 0.6)
    Amenities_txt = str(r.get("Amenities", "")).strip()
    amenity_count = 0 if Amenities_txt == "" else len([s for s in Amenities_txt.split(",") if s.strip() != ""])
    amenity_score = amenity_count / max(1, 5)
    age = float(CURRENT_YEAR - year_built)
    floor_ratio = (floor_no / total_floors) if total_floors > 0 else 0.0
    price_per_bhk = price / max(bhk, 1)
    size_per_bhk = size / max(bhk, 1)
    transport_weighted = transport_score * ppsf
    infra_density = (school_score + hosp_score) / 2
    efficiency = ppsf * size
    security_score = 1.0 if str(r.get("Security", "No")).lower() in ("yes", "y", "gated", "cctv", "guard") else 0.0
    city_rank = r.get("City_Price_Rank", 0.5)
    locality_rank = r.get("Locality_PPSF_Rank", 0.5)
    locality_hotspot = r.get("Locality_Hotspot_Score", 0.5)
    age_cat = "New" if age <= 10 else ("Mid" if age <= 20 else "Old")

    final = {
        "Size_in_SqFt": size,
        "PPSF_Recalc": ppsf,
        "School_Density_Score": school_score,
        "Hospital_Density_Score": hosp_score,
        "Transport_Score": transport_score,
        "Amenity_Count": amenity_count,
        "Age_of_Property": age,
        "City_Price_Rank": city_rank,
        "Locality_PPSF_Rank": locality_rank,
        "Floor_Ratio": floor_ratio,
        "Amenity_Score": amenity_score,
        "Security_Score": security_score,
        "Transport_Weighted": transport_weighted,
        "Infra_Density": infra_density,
        "Efficiency": efficiency,
        "Price_per_BHK": price_per_bhk,
        "Size_per_BHK": size_per_bhk,
        "Locality_Hotspot_Score": locality_hotspot,
        "Age_Category": age_cat,
        # categorical originals
        "State": str(r.get("State", dd["State"])),
        "City": str(r.get("City", dd["City"])),
        "Locality": str(r.get("Locality", dd["Locality"])),
        "Property_Type": str(r.get("Property_Type", dd["Property_Type"])),
        "Furnished_Status": str(r.get("Furnished_Status", dd["Furnished_Status"])),
        "Parking_Space": str(r.get("Parking_Space", dd["Parking_Space"])),
        "Security": str(r.get("Security", dd["Security"])),
        "Facing": str(r.get("Facing", dd["Facing"])),
        "Owner_Type": str(r.get("Owner_Type", dd["Owner_Type"])),
        "Availability_Status": str(r.get("Availability_Status", dd["Availability_Status"])),
    }
    return final

# -------------------------
# Prediction wrapper
# -------------------------
def predict_row(row_dict: Dict, use_rf_flag=True, use_xgb_flag=True, use_clf_flag=True):
    eng = build_engineered_row(row_dict)
    X_df = pd.DataFrame([eng])
    out = {"engineered": eng}

    # classifier
    clf = art.get("clf")
    if use_clf_flag and clf is not None:
        try:
            out["Good_Investment_Label"] = int(clf.predict(X_df)[0])
            # some classifiers may not have predict_proba
            out["Good_Investment_Prob"] = float(clf.predict_proba(X_df)[:, 1][0]) if hasattr(clf, "predict_proba") else None
        except Exception as e:
            out["clf_error"] = str(e)
            out["Good_Investment_Label"] = None
            out["Good_Investment_Prob"] = None
    else:
        out["Good_Investment_Label"] = None
        out["Good_Investment_Prob"] = None

    # regressors (apply inverse scaling if scales provided)
    scales = art.get("scales", {})
    rf_scale = float(scales.get("RF_SCALE", 1.0))
    xgb_scale = float(scales.get("XGB_SCALE", 1.0))
    if use_rf_flag and art.get("reg_rf") is not None:
        try:
            raw = art["reg_rf"].predict(X_df)[0]
            out["Future_Price_5Y_RF_raw"] = float(raw)
            out["Future_Price_5Y_RF"] = float(raw / rf_scale)
        except Exception as e:
            out["reg_rf_error"] = str(e)
    if use_xgb_flag and art.get("reg_xgb") is not None:
        try:
            raw = art["reg_xgb"].predict(X_df)[0]
            out["Future_Price_5Y_XGB_raw"] = float(raw)
            out["Future_Price_5Y_XGB"] = float(raw / xgb_scale)
        except Exception as e:
            out["reg_xgb_error"] = str(e)

    return out

# -------------------------
# UI: Single property
# -------------------------
if mode == "Single property":
    st.header("Single property prediction")
    col1, col2 = st.columns([2, 1])
    with col1:
        price = st.slider("Current Price (Lakhs)", 10.0, 500.0, 254.0, step=1.0)
        size = st.slider("Size (SqFt)", 500, 5000, 2750, step=50)
        bhk = st.selectbox("BHK", [1, 2, 3, 4, 5], index=2)
        year_built = st.number_input("Year Built", min_value=1990, max_value=CURRENT_YEAR, value=2006)
        schools = st.slider("Nearby Schools (count)", 0, 10, 5)
        hospitals = st.slider("Nearby Hospitals (count)", 0, 10, 5)
        transport = st.selectbox("Public Transport Accessibility", ["Low", "Medium", "High"], index=1)
        amenities = st.text_input("Amenities (comma-separated)", value="Gym,Pool,Clubhouse")
    with col2:
        property_type = st.selectbox("Property Type", ["Apartment", "Independent House", "Villa"])
        furnished = st.selectbox("Furnished Status", ["Furnished", "Semi-furnished", "Unfurnished"])
        parking = st.selectbox("Parking Space", ["Yes", "No"])
        security = st.selectbox("Security", ["Yes", "No"])
        facing = st.selectbox("Facing", ["North", "South", "East", "West"])
        owner_type = st.selectbox("Owner Type", ["Owner", "Broker", "Builder"])
        availability = st.selectbox("Availability Status", ["Ready_to_Move", "Under_Construction"])
        state = st.text_input("State", "Karnataka")
        city = st.text_input("City", "Bangalore")
        locality = st.text_input("Locality", "Locality_1")

    if st.button("Predict for this property"):
        inp = dict(
            Price_in_Lakhs=price,
            Size_in_SqFt=size,
            BHK=bhk,
            Year_Built=year_built,
            Nearby_Schools=schools,
            Nearby_Hospitals=hospitals,
            Public_Transport_Accessibility=transport,
            Amenities=amenities,
            Furnished_Status=furnished,
            Floor_No=1,
            Total_Floors=1,
            Parking_Space=parking,
            Security=security,
            Facing=facing,
            Property_Type=property_type,
            Owner_Type=owner_type,
            Availability_Status=availability,
            State=state,
            City=city,
            Locality=locality,
        )
        out = predict_row(inp, use_rf_flag=use_rf, use_xgb_flag=use_xgb, use_clf_flag=use_clf)
        st.subheader("Results")
        if out.get("Good_Investment_Label") is not None:
            st.metric("Good Investment (classifier)", int(out["Good_Investment_Label"]),
                      delta=None)
            prob = out.get("Good_Investment_Prob")
            if prob is not None:
                st.write(f"Probability: {prob:.4f}")
        if "Future_Price_5Y_RF" in out:
            st.write("Future Price (RF, 5Y):", out["Future_Price_5Y_RF"])
        if "Future_Price_5Y_XGB" in out:
            st.write("Future Price (XGB, 5Y):", out["Future_Price_5Y_XGB"])
        if show_debug:
            st.json(out["engineered"])

# -------------------------
# UI: CSV batch predict
# -------------------------
elif mode == "CSV batch predict":
    st.header("Batch predict from CSV")
    st.markdown("Upload a CSV containing at least: Price_in_Lakhs, Size_in_SqFt, BHK, Year_Built, Nearby_Schools, Nearby_Hospitals, Public_Transport_Accessibility, Amenities. Extra columns are preserved.")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded)
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")
            df = None
        if df is not None:
            st.write("Preview:", df.head())
            if st.button("Run batch predictions"):
                preds = []
                for _, r in df.iterrows():
                    rd = r.to_dict()
                    p = predict_row(rd, use_rf_flag=use_rf, use_xgb_flag=use_xgb, use_clf_flag=use_clf)
                    out_row = {
                        "Future_Price_5Y_RF": p.get("Future_Price_5Y_RF"),
                        "Future_Price_5Y_XGB": p.get("Future_Price_5Y_XGB"),
                        "Good_Investment_Label": p.get("Good_Investment_Label"),
                        "Good_Investment_Prob": p.get("Good_Investment_Prob"),
                    }
                    preds.append(out_row)
                preds_df = pd.DataFrame(preds)
                result = pd.concat([df.reset_index(drop=True), preds_df.reset_index(drop=True)], axis=1)
                st.write(result.head())
                csv_bytes = result.to_csv(index=False).encode("utf-8")
                st.download_button("Download predictions CSV", data=csv_bytes, file_name="predictions.csv")

# -------------------------
# UI: Explore & Visualize
# -------------------------
else:
    st.header("Explore & Visualize (quick)")
    st.markdown("Upload a CSV for quick histograms and a model-agreement scatter (small sample).")
    uploaded = st.file_uploader("Upload CSV to visualize", type=["csv"], key="viz")
    if uploaded is not None:
        try:
            dfv = pd.read_csv(uploaded)
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")
            dfv = None
        if dfv is not None:
            st.write("Preview:", dfv.head())
            numeric_cols = [c for c in dfv.columns if pd.api.types.is_numeric_dtype(dfv[c])]
            if numeric_cols:
                col = st.selectbox("Numeric column to plot", numeric_cols)
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.hist(dfv[col].dropna(), bins=40)
                ax.set_title(f"Distribution — {col}")
                st.pyplot(fig)
            if st.button("Run small predictions (visual)"):
                sample = dfv.sample(min(len(dfv), 1000), random_state=42)
                preds = []
                for _, r in sample.iterrows():
                    p = predict_row(r.to_dict(), use_rf_flag=use_rf, use_xgb_flag=use_xgb, use_clf_flag=use_clf)
                    preds.append(p)
                pr = pd.DataFrame(preds)
                st.write("Predictions sample:", pr.head())
                if ("Future_Price_5Y_RF" in pr.columns) and ("Future_Price_5Y_XGB" in pr.columns):
                    fig, ax = plt.subplots(figsize=(6, 4))
                    ax.scatter(pr["Future_Price_5Y_RF"], pr["Future_Price_5Y_XGB"], alpha=0.5)
                    ax.set_xlabel("RF future")
                    ax.set_ylabel("XGB future")
                    ax.set_title("RF vs XGB predictions")
                    st.pyplot(fig)

# -------------------------
# Footer / artifact warnings
# -------------------------
st.sidebar.markdown("---")
st.sidebar.caption("Place a ./models folder with your saved artifacts next to this file. If models are missing the app still runs but predictions will be unavailable where appropriate.")

# show artifact status briefly
with st.expander("Artifacts status"):
    st.write({
        "classifier_loaded": art.get("clf") is not None,
        "regressor_rf_loaded": art.get("reg_rf") is not None,
        "regressor_xgb_loaded": art.get("reg_xgb") is not None,
        "preprocessor_loaded": art.get("preprocessor") is not None,
        "scales_present": bool(art.get("scales"))
    })
