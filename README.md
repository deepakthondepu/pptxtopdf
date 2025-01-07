# PPTX to PDF Converter

This project is a Flask-based REST API that converts PowerPoint (.pptx) files into PDF files.
---
## Features
- Upload `.pptx` files via a POST request.
- Extracts text from slides and converts it into a PDF.
- Interactive API documentation with Swagger UI.
---
## Setup Instructions
1. Clone the repository:
   git clone https://github.com/deepakthondepu/pptxtopdf.git
   # Navigate to the project directory
   cd pptxtopdf

2. Create and activate a virtual environment:
	python -m venv venv
	venv\Scripts\activate

3. Install dependencies:
	pip install -r requirements.txt

4. Start the Flask application:
	python app.py

5.Click on the URL in terminal:
	http://127.0.0.1:5000/
