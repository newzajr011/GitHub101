# OCR Web Application (เว็บแอปพลิเคชัน OCR)

This is a simple web application that allows users to upload image files (PNG, JPG) and PDF documents to extract text from them. The application uses the Tesseract OCR engine and supports both English and Thai languages.

เว็บแอปพลิเคชันอย่างง่ายสำหรับอัปโหลดไฟล์รูปภาพ (PNG, JPG) และเอกสาร PDF เพื่อดึงข้อความออกมาโดยใช้ Tesseract OCR ซึ่งรองรับทั้งภาษาอังกฤษและภาษาไทย

## Requirements (สิ่งที่ต้องมี)

- **Tesseract OCR Engine:** The core OCR engine.
- **Python 3**
- **Python Libraries:**
  - `Flask`
  - `Pillow`
  - `pytesseract`
  - `PyMuPDF`

## Installation (การติดตั้ง)

1.  **Install Tesseract OCR Engine and Language Packs:**
    (ติดตั้ง Tesseract OCR และแพ็คภาษาไทย)

    For Debian/Ubuntu-based systems:
    ```bash
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr tesseract-ocr-tha
    ```

2.  **Install Python Libraries:**
    (ติดตั้งไลบรารีของ Python)
    ```bash
    pip install Flask Pillow pytesseract PyMuPDF
    ```

## How to Run (วิธีการรันโปรแกรม)

1.  **Run the Flask application:**
    (รันเว็บแอปพลิเคชัน)
    ```bash
    python3 app.py
    ```

2.  **Access the application:**
    (เข้าถึงแอปพลิเคชัน)
    Open your web browser and navigate to:
    [http://localhost:8080](http://localhost:8080)

You can then upload a file to start the OCR process.
จากนั้นคุณสามารถอัปโหลดไฟล์เพื่อเริ่มกระบวนการ OCR ได้ทันที
