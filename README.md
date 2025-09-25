# Gemini Image Generator App - Nano GPT 🎋

A Streamlit web application that generates amazing images using Google's Gemini Nnao AI model. This project is designed for workshop demonstrations and learning purposes.

![Streamlit -app (1)](https://github.com/user-attachments/assets/a2e2a7e5-cf9d-4dc8-bb85-001ddf8685d6)



## Features

-  Generate images from text prompts using Google Gemini AI
-  Beautiful and intuitive web interface built with Streamlit
-  Download generated images in PNG format
-  Secure API key management
-  Docker support for easy deployment

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Docker (optional, for containerized deployment)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Raghul-M/Gemini-Image-app
cd Gemini-Image-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
3. You can enter your API key directly in the application's sidebar.

### 4. Run the Application Locally

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Docker Deployment

### Build Docker Image

```bash
docker build -t gemini-image-app .
```

### Run Docker Container

```bash
docker run -d --name nanogpt -p 8501:8501 -e  gemini-image-app
```

### Push to Docker Registry

```bash
# Tag the image
docker tag gemini-image-app docker.io/raghulm/gemini-image-app:latest

# Push to registry
docker push docker.io/raghulm/gemini-image-app:latest
```

## Usage

1. Open the application in your web browser
2. Enter your Gemini API key in the sidebar (or set it as an environment variable)
3. Type your image prompt in the text input field
4. Click "Generate Image" and wait for the AI to create your image
5. Download the generated image using the download button

## Example Prompts

- "A beautiful sunset over a calm ocean"
- "A futuristic city with flying cars"
- "A cute cat wearing a space helmet"
- "Abstract art with vibrant colors"

## Project Structure

```
Gemini-Image-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── .env              # Environment variables (create this)
└── README.md         # This file
```

## Technologies Used

- **Streamlit** - Web application framework
- **Google Gemini AI** - Image generation API
- **Pillow (PIL)** - Image processing
- **Python-dotenv** - Environment variable management
- **Docker** - Containerization

## API Key Setup

To get your Gemini API key:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file or enter it in the app

## Troubleshooting

- **API Key Error**: Make sure your Gemini API key is valid and has the necessary permissions
- **Image Generation Fails**: Check your internet connection and API key status
- **Docker Issues**: Ensure Docker is running and you have sufficient permissions

## Contributing

This is a workshop project. Feel free to fork and modify for your own learning purposes!

## License

This project is open source and available under the [MIT License](LICENSE).


Built with ❤️ By Raghul-M using Streamlit and Google Gemini AI
