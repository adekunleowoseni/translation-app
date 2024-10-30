# Translation Web App

A simple web application that translates text between different languages using the Google Translate API.

## Features

- Clean, responsive interface
- Support for multiple languages
- Real-time translation
- Simple and easy to use

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/adekunleowoseni/translation-app.git
cd translation-app
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter the text you want to translate in the text area
2. Select the target language from the dropdown menu
3. Click the "Translate" button
4. The translated text will appear below the form

## Dependencies

- Flask==2.0.1
- requests==2.26.0
- googletrans==3.1.0a0

## Notes

- This application uses the unofficial Google Translate API
- For production use, consider using the official Google Cloud Translation API
- The application includes a responsive design that works on both desktop and mobile devices