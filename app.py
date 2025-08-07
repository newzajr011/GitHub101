import os
import io
import fitz  # PyMuPDF
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract

# --- Configuration ---
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'supersecretkey'  # Needed for flash messages

# --- Helper Functions ---
def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ocr_process(filepath):
    """Perform OCR on the given file (image or PDF)."""
    filename = os.path.basename(filepath)
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    text = ""

    try:
        if extension in ['.png', '.jpg', '.jpeg']:
            # Use Pillow to open the image and Pytesseract to extract text
            # Specify both English and Thai languages
            text = pytesseract.image_to_string(Image.open(filepath), lang='eng+tha')
        elif extension == '.pdf':
            # Use PyMuPDF to open the PDF
            doc = fitz.open(filepath)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                img_data = pix.tobytes("png")
                img = Image.open(io.BytesIO(img_data))
                # Append text from each page, specifying both languages
                text += pytesseract.image_to_string(img, lang='eng+tha') + "\\n\\n"
            doc.close()
        else:
            return "Unsupported file type."
    except Exception as e:
        return f"An error occurred during OCR processing: {e}"

    return text

# --- Routes ---
@app.route('/')
def index():
    """Render the main upload page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and OCR processing."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Ensure the upload folder exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Perform OCR
        extracted_text = ocr_process(filepath)

        # Clean up the uploaded file
        os.remove(filepath)

        return render_template('result.html', extracted_text=extracted_text)
    else:
        flash('File type not allowed. Please upload a PNG, JPG, or PDF file.')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
