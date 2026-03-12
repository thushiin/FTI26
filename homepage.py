import streamlit as st
import importlib

st.set_page_config(page_title="FTI2026", layout="wide", initial_sidebar_state="expanded")

region_modules = {
    "All Regions": "main_dashboard",
    "Muscat": "MCT",
    "Ad Dakhliyah": "DKL",
    "Ash Sharqiyah South": "SHS",
    "Ash Sharqiyah North": "SHN",
    "Al Wusta": "WST",
    "Al Batinah North": "BTN",
    "Al Batinah South": "BTS",
    "Musandam": "MSD",
    "Adh Dhahirah": "DHR",
    "Buraimi":"BRM"
}

cluster_map = {
    "All Regions": ["Muscat", "Ash Sharqiyah North", "Ash Sharqiyah South",
                    "Al Batinah North", "Adh Dhahirah", "Musandam",
                    "Ad Dakhliyah", "Al Batinah South", "Al Wusta","Buraimi"],
    "Cluster 1": ["Muscat", "Ash Sharqiyah North", "Ash Sharqiyah South"],
    "Cluster 2": ["Al Batinah North", "Adh Dhahirah", "Musandam"],
    "Cluster 3": ["Ad Dakhliyah", "Al Batinah South", "Al Wusta", "Buraimi"],
    
}

# Only cluster selection
selected_cluster = st.sidebar.radio(
    "Select Cluster",
    options=list(cluster_map.keys()),
    label_visibility="collapsed"
)

# -------------------- PAGE ROUTING --------------------
# Decide which module to load based on cluster
if selected_cluster == "Cluster 1":
    module_name = "cluster1"  # You can choose which cluster uses main_dashboard
elif selected_cluster == "Cluster 2":
    module_name = "cluster2"
elif selected_cluster == "Cluster 3":
    module_name = "cluster3"
else:
    module_name = "main_dashboard"

# -------------------- FOOTER --------------------
st.sidebar.markdown(
    """
    <style>
    .last-updated {
        position: fixed;
        bottom: 10px;
        left: 10px;
        font-size: 12px;
        color: gray;
    }
    </style>
    <div class="last-updated">
        Last updated on: 31-01-2026
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- LOAD PAGE --------------------
module = importlib.import_module(module_name)
module.run()







