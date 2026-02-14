import streamlit as st
import os
import hashlib
from PIL import Image
import matplotlib.pyplot as plt
import cv2
st.markdown("""
    <style>
    .stApp {
        background-color: #f0fff4;
    }
    h1, h2, h3 {
        color: #14532d;
    }
    .stButton>button {
        background-color: #16a34a;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Digital Decay", layout="wide")

# ================= SESSION =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ================= LOGIN SYSTEM =================
def login():
    st.title("🔐 Digital Decay Login")
    st.markdown("---")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Credentials ❌")

def logout():
    st.session_state.logged_in = False
    st.rerun()

# ================= IMAGE FUNCTIONS =================
def is_blurry(image_path, threshold=100):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance < threshold

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# ================= MAIN APP =================
def main_app():

    st.title("🌱 Digital Decay")
    st.caption("Clean Your Cloud. Reduce Digital Carbon.")
    st.sidebar.button("🚪 Logout", on_click=logout)

    folder_path = st.text_input("📂 Enter Folder Path to Scan")

    if folder_path and os.path.exists(folder_path):

        image_files = [
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]

        # ===== BLUR DETECTION =====
        blurry_images = [img for img in image_files if is_blurry(img)]
        blurry_count = len(blurry_images)

        # ===== DUPLICATE DETECTION (HASH BASED) =====
        hash_map = {}
        duplicate_files = []

        for file in image_files:
            file_hash = get_file_hash(file)
            if file_hash in hash_map:
                duplicate_files.append(file)
            else:
                hash_map[file_hash] = file

        duplicates = len(duplicate_files)

        # ===== STORAGE + CO2 =====
        total_size = sum(os.path.getsize(f) for f in image_files)
        storage_gb = round(total_size / (1024**3), 3)
        co2 = round(storage_gb * 0.5, 3)

        # ================= DASHBOARD =================
        st.markdown("## 📊 Dashboard Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("📁 Duplicates", duplicates)
        col2.metric("🖼 Blurry", blurry_count)
        col3.metric("💾 Storage (GB)", storage_gb)
        col4.metric("🌍 CO₂ (kg)", co2)

        # ===== SMALL GRAPH =====
        st.markdown("### 📊 Waste Overview")

        # count of original (unique) images
        originals = len(hash_map)  # unique hashes => original images

        fig, ax = plt.subplots(figsize=(5,3))
        labels = ["Originals", "Duplicates", "Blurry"]
        values = [originals, duplicates, blurry_count]
        colors = ["#16a34a", "#f59e0b", "#ef4444"]
        ax.bar(labels, values, color=colors)
        ax.set_ylabel("Count")
        for i, v in enumerate(values):
            ax.text(i, v + 0.05, str(v), ha='center', va='bottom')
        st.pyplot(fig)

        st.markdown("---")

        # ===== VIEW SWITCH =====
        view = st.radio("Select View", ["Blurry Images", "Duplicate Files"], horizontal=True)

        # ================= BLURRY VIEW =================
        if view == "Blurry Images":

            st.subheader("🖼 Blurry Images")

            select_all = st.checkbox("Select All")
            selected_files = []

            for file in blurry_images:
                col1, col2, col3 = st.columns([1,3,1])

                with col1:
                    checked = st.checkbox("", key=file, value=select_all)

                with col2:
                    st.image(Image.open(file), width=200)

                with col3:
                    if st.button("Delete", key="blur_"+file):
                        os.remove(file)
                        st.success("Deleted Successfully ✅")
                        st.rerun()

                if checked:
                    selected_files.append(file)

            if st.button("Delete Selected"):
                for f in selected_files:
                    os.remove(f)
                st.success("Selected Blurry Images Deleted ✅")
                st.rerun()

        # ================= DUPLICATE VIEW =================
        if view == "Duplicate Files":

            st.subheader("📁 Duplicate Files")

            select_all = st.checkbox("Select All", key="dup_all")
            selected_files = []

            for file in duplicate_files:
                col1, col2, col3 = st.columns([1,3,1])

                with col1:
                    checked = st.checkbox("", key="dup_"+file, value=select_all)

                with col2:
                    st.image(Image.open(file), width=200)

                with col3:
                    if st.button("Delete", key="del_dup_"+file):
                        os.remove(file)
                        st.success("Deleted Successfully ✅")
                        st.rerun()

                if checked:
                    selected_files.append(file)

            if st.button("Delete Selected", key="delete_dup"):
                for f in selected_files:
                    os.remove(f)
                st.success("Selected Duplicate Files Deleted ✅")
                st.rerun()

    else:
        st.info("Enter a valid folder path to begin scanning.")

# ================= RUN =================
if st.session_state.logged_in:
    main_app()
else:
    login()