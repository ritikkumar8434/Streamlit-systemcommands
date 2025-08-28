# commandhub.py

import streamlit as st
import subprocess

st.set_page_config(page_title="CommandHub", layout="wide")

st.title("⚡ CommandHub – Linux Command Center")
st.write("Run predefined system commands OR enter your own safely from the WebUI.")

# -----------------------
# Helper function
# -----------------------
def run_command(command: str):
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

# -----------------------
# Section 1: Predefined Commands
# -----------------------
st.subheader("🔥 Quick Commands")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📂 List Files (ls -la)"):
        out, err = run_command("ls -la")
        st.code(out if out else err)

with col2:
    if st.button("🖥 Uptime"):
        out, err = run_command("uptime")
        st.code(out if out else err)

with col3:
    if st.button("💾 Disk Usage (df -h)"):
        out, err = run_command("df -h")
        st.code(out if out else err)

with col4:
    if st.button("📊 Memory Usage (free -m)"):
        out, err = run_command("free -m")
        st.code(out if out else err)

# -----------------------
# Section 2: Custom Command Input
# -----------------------
st.subheader("🛠 Run Custom Command")

user_cmd = st.text_input("Enter your command:", value="echo Hello CommandHub")
if st.button("Run Custom Command"):
    st.info(f"Running: `{user_cmd}`")
    out, err = run_command(user_cmd)
    if out:
        st.subheader("Output")
        st.code(out)
    if err:
        st.subheader("Error")
        st.code(err)
