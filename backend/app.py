from pathlib import Path
import uuid

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from ocr_engine import ocr_pdf_bytes, make_searchable_pdf_bytes

app = FastAPI(title="Local PDF OCR")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ocr")
async def ocr_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are supported right now."}

    pdf_bytes = await file.read()
    pages = ocr_pdf_bytes(pdf_bytes)

    return {
        "filename": file.filename,
        "pages": pages
    }


@app.post("/ocr-text-file")
async def ocr_pdf_to_text_file(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are supported right now."}

    pdf_bytes = await file.read()
    pages = ocr_pdf_bytes(pdf_bytes)

    output_text = []

    for page in pages:
        output_text.append(f"\n\n--- Page {page['page']} ---\n")
        output_text.append(page["text"])

    output_id = str(uuid.uuid4())
    output_path = OUTPUT_DIR / f"ocr_output_{output_id}.txt"

    output_path.write_text("\n".join(output_text), encoding="utf-8")

    return FileResponse(
        output_path,
        media_type="text/plain",
        filename=f"{file.filename}_ocr.txt"
    )


@app.post("/ocr-searchable-pdf")
async def ocr_pdf_to_searchable_pdf(
    file: UploadFile = File(...),
    quality: str = "fast"
):
    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are supported right now."}

    pdf_bytes = await file.read()

    if quality == "high":
        dpi = 300
    else:
        dpi = 200

    searchable_pdf_bytes = make_searchable_pdf_bytes(pdf_bytes, dpi=dpi)

    output_id = str(uuid.uuid4())
    output_path = OUTPUT_DIR / f"searchable_{output_id}.pdf"

    output_path.write_bytes(searchable_pdf_bytes)

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename=f"{file.filename}_searchable.pdf"
    )