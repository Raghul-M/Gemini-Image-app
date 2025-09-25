import streamlit as st
from google import genai
from dotenv import load_dotenv
import base64
import mimetypes
import os
from google.genai import types
import io
from PIL import Image

load_dotenv()

st.title("Gemini Nano GPT 🎋")
st.markdown("Generate amazing images using Google's Gemini Nano AI model!")


# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Gemini API Key", type="password", value=os.environ.get("GEMINI_API_KEY", ""))
    if not api_key:
        st.warning("Please enter your Gemini API key in the sidebar or set it as an environment variable.")

# Main interface
prompt = st.text_input("Enter your prompt", placeholder="e.g. A beautiful sunset over a calm ocean")

generate_button = st.button("Generate Image", type="primary", disabled=not api_key)

# To run this code you need to install the following dependencies:
# pip install google-genai




def generate_image_with_gemini(prompt_text, api_key):
    """Generate an image using Gemini API and return it as a PIL Image"""
    try:
        client = genai.Client(api_key=api_key)
        
        model = "gemini-2.5-flash-image-preview"
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt_text),
                ],
            ),
        ]
        generate_content_config = types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        )

        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if (
                chunk.candidates is None
                or chunk.candidates[0].content is None
                or chunk.candidates[0].content.parts is None
            ):
                continue
                
            if (chunk.candidates[0].content.parts[0].inline_data and 
                chunk.candidates[0].content.parts[0].inline_data.data):
                
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                data_buffer = inline_data.data
                
                # Convert binary data to PIL Image
                image = Image.open(io.BytesIO(data_buffer))
                return image
                
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return None

# Main image generation logic
if generate_button and prompt and api_key:
    with st.spinner("Generating your image... This may take a few moments."):
        generated_image = generate_image_with_gemini(prompt, api_key)
        
        if generated_image:
            st.success("Image generated successfully!")
            
            # Display the image
            st.image(generated_image, caption=f"Generated: {prompt}", use_container_width=True)
            
            # Add download button for the current image
            img_buffer = io.BytesIO()
            generated_image.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            
            st.download_button(
                label="Download Image",
                data=img_buffer.getvalue(),
                file_name=f"gemini_image_{prompt[:30].replace(' ', '_')}.png",
                mime="image/png",
                key="download_current_image"
            )


# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Google Gemini Nano AI")
