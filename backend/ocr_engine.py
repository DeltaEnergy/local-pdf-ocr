import io
import sys
from pathlib import Path

import fitz
import pytesseract
from PIL import Image
from pypdf import PdfReader, PdfWriter


def get_app_base_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    return Path(__file__).resolve().parent


BASE_DIR = get_app_base_path()

BUNDLED_TESSERACT_EXE = BASE_DIR / "tesseract" / "tesseract.exe"
BUNDLED_TESSDATA_DIR = BASE_DIR / "tesseract" / "tessdata"

SYSTEM_TESSERACT_EXE = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
SYSTEM_TESSDATA_DIR = Path(r"C:\Program Files\Tesseract-OCR\tessdata")


if BUNDLED_TESSERACT_EXE.exists():
    pytesseract.pytesseract.tesseract_cmd = str(BUNDLED_TESSERACT_EXE)
    ACTIVE_TESSDATA_DIR = BUNDLED_TESSDATA_DIR
elif SYSTEM_TESSERACT_EXE.exists():
    pytesseract.pytesseract.tesseract_cmd = str(SYSTEM_TESSERACT_EXE)
    ACTIVE_TESSDATA_DIR = SYSTEM_TESSDATA_DIR
else:
    ACTIVE_TESSDATA_DIR = None


def get_config() -> str:
    if ACTIVE_TESSDATA_DIR and ACTIVE_TESSDATA_DIR.exists():
        tessdata_path = str(ACTIVE_TESSDATA_DIR).replace("\\", "/")
        return f"--tessdata-dir {tessdata_path} --oem 3 --psm 6"

    return "--oem 3 --psm 6"


def ocr_pdf_bytes(pdf_bytes: bytes, dpi: int = 200):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []

    config = get_config()

    for page_index in range(len(doc)):
        page = doc[page_index]

        pix = page.get_pixmap(dpi=dpi)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))

        text = pytesseract.image_to_string(
            image,
            lang="eng",
            config=config
        )

        pages.append({
            "page": page_index + 1,
            "text": text
        })

    return pages


def make_searchable_pdf_bytes(pdf_bytes: bytes, dpi: int = 200) -> bytes:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    writer = PdfWriter()

    config = get_config()

    for page_index in range(len(doc)):
        page = doc[page_index]

        pix = page.get_pixmap(dpi=dpi)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))

        searchable_page_pdf = pytesseract.image_to_pdf_or_hocr(
            image,
            extension="pdf",
            lang="eng",
            config=config
        )

        reader = PdfReader(io.BytesIO(searchable_page_pdf))
        writer.add_page(reader.pages[0])

    output = io.BytesIO()
    writer.write(output)

    return output.getvalue()