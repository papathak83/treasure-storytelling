import streamlit as st
from PIL import Image
import os
import random

# Ρύθμιση του φακέλου με τις εικόνες
folder_path = "C:/Users/papat/OneDrive/Documents/storytelling/treasure hunter/treasure-hunter/"

def get_random_image(position):
    """Επιστρέφει τυχαία εικόνα για μια συγκεκριμένη θέση."""
    valid_filenames = [f"{(position - 1) * 5 + j}.png" for j in range(1, 6)]
    images = [img for img in valid_filenames if img in os.listdir(folder_path)]
    
    if images:
        return os.path.join(folder_path, random.choice(images))
    return None

# --- Streamlit UI ---
st.set_page_config(page_title="Πες μια Ιστορία - Web App", layout="wide")

st.title("🎭 Πες μια Ιστορία - Κυνήγι Θησαυρού")

# Αν δεν υπάρχουν αποθηκευμένες εικόνες, δημιουργούμε τυχαίες αρχικές εικόνες
if "selected_images" not in st.session_state:
    st.session_state.selected_images = [get_random_image(i + 1) for i in range(5)]

# Στήλες για τις 5 εικόνες
cols = st.columns(5)
titles = ["Ήρωας", "Στοιχείο", "Εμπόδιο", "Βοηθός", "Τέλος"]

for i, col in enumerate(cols):
    with col:
        st.subheader(titles[i])

        # Προβολή αποθηκευμένης εικόνας
        img_path = st.session_state.selected_images[i]
        if img_path:
            img = Image.open(img_path)
            st.image(img, use_container_width=True)  # Αντικαταστάθηκε το use_column_width με use_container_width

        # Κουμπί επιλογής νέας εικόνας
        if st.button(f"🎰 Επιλογή {titles[i]}", key=f"button_{i}"):
            st.session_state.selected_images[i] = get_random_image(i + 1)
            st.rerun()
