import streamlit as st
from pathlib import Path

st.title("📁 File Management Tool")

# Function to get all files and folders
def get_files():
    path = Path('.')
    return list(path.rglob('*'))

# List all files/folders
st.subheader("📄 Files and Folders in Current Directory:")
files = get_files()
if files:
    for i, item in enumerate(files):
        st.write(f"{i + 1}: {item}")
else:
    st.write("No files or folders found.")

# Operation selection
operation = st.selectbox("Choose an operation:", ["Create", "Read", "Update", "Delete"])

filename = st.text_input("Enter the file name:")

# Create File
if operation == "Create":
    content = st.text_area("Enter content to write in file:")
    if st.button("Create File"):
        p = Path(filename)
        if not p.exists():
            try:
                with open(p, 'w') as f:
                    f.write(content)
                st.success(f"✅ File '{filename}' created successfully.")
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
        else:
            st.warning(f"⚠️ File '{filename}' already exists.")

# Read File
elif operation == "Read":
    if st.button("Read File"):
        p = Path(filename)
        if p.exists() and p.is_file():
            try:
                with open(p, 'r') as f:
                    st.text_area("📄 File Contents:", f.read(), height=300)
                st.success("✅ File read successfully.")
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
        else:
            st.error("❌ File does not exist.")

# Update File
elif operation == "Update":
    new_content = st.text_area("What do you want to append?")
    if st.button("Update File"):
        p = Path(filename)
        if p.exists() and p.is_file():
            try:
                with open(p, 'a') as f:
                    f.write("\n" + new_content)
                st.success("✅ File updated successfully.")
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
        else:
            st.error("❌ File does not exist.")

# Delete File
elif operation == "Delete":
    if st.button("Delete File"):
        p = Path(filename)
        if p.exists() and p.is_file():
            try:
                p.unlink()
                st.success("🗑️ File deleted successfully.")
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
        else:
            st.error("❌ File does not exist.")
