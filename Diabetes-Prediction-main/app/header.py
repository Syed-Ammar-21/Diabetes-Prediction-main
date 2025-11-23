import streamlit as st
import base64
import io
from PIL import Image
from data.base import head_template, st_style, footer


def app():
    st.markdown(st_style, 
            unsafe_allow_html=True)

    st.markdown(footer, 
                unsafe_allow_html=True)

    # Load and encode the logo image with transparent background
    try:
        logo_image = Image.open("image/page_icon.jpeg")
        
        # Convert to RGBA if not already
        if logo_image.mode != 'RGBA':
            logo_image = logo_image.convert('RGBA')
        
        # Remove white/light background (make it transparent)
        data = logo_image.getdata()
        new_data = []
        for item in data:
            # If pixel is white or very light (threshold for white removal)
            # You can adjust the threshold (255, 255, 255) to be more or less strict
            if item[0] > 240 and item[1] > 240 and item[2] > 240:  # White/light pixels
                new_data.append((255, 255, 255, 0))  # Make transparent
            else:
                new_data.append(item)  # Keep original pixel
        
        logo_image.putdata(new_data)
        
        # Convert image to base64 as PNG (supports transparency)
        buffer = io.BytesIO()
        logo_image.save(buffer, format='PNG')
        logo_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        # Format the head template with the logo
        head = head_template.format(logo_base64=logo_base64)
    except Exception as e:
        # Fallback if image can't be loaded
        head = head_template.format(logo_base64="")
        st.warning(f"Could not load logo: {e}")

    st.markdown(head, 
        unsafe_allow_html=True
    )