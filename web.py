import streamlit as st

# Define logos as Base64 strings or URLs.
left_logo = "https://github.com/Irfanmrd12/streamlit/blob/main/images.png?raw=true"
right_logo1 = "https://github.com/Irfanmrd12/streamlit/blob/main/images.png?raw=true"
right_logo2 = "https://github.com/Irfanmrd12/streamlit/blob/main/images.png?raw=true"

header_html = f"""
<style>
    .header-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}

    .header-container img {{
        max-height: 50px;
        margin: 5px;
    }}
</style>

<div class="header-container">
    <img src="{left_logo}" alt="left-logo">
    <div>
        <img src="{right_logo1}" alt="right-logo1">
        <img src="{right_logo2}" alt="right-logo2">
    </div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)
