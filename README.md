

# Local PDF OCR

Local PDF OCR is a privacy-focused OCR tool for Firefox and Waterfox. It converts scanned or image-based PDFs into searchable PDFs using a local backend. Files are processed on the user's computer and are not uploaded to a cloud service.

## Features

* Convert scanned PDFs into searchable PDFs
* Local OCR processing
* Browser extension interface
* FastAPI backend
* Tesseract OCR engine
* Works with screenshot-heavy PDFs, receipts, forms, and scanned documents

## Current Status

This is an early prototype.

### Working

* Local backend
* PDF upload
* OCR text extraction
* Searchable PDF output
* Firefox/Waterfox extension upload page

### Known Limitations

* OCR accuracy depends on scan quality
* Complex layouts, maps, receipts, and tiny screenshot text may be imperfect
* Backend must be started before using the extension

## Installing the Extension

This extension is currently loaded manually as a temporary extension.

### Firefox

1. Open Firefox.
2. Go to:

```txt
about:debugging#/runtime/this-firefox
```

3. Click **Load Temporary Add-on**.
4. Select the extension's `manifest.json` file.
5. The extension should now appear in Firefox.

### Waterfox

1. Open Waterfox.
2. Go to:

```txt
about:debugging#/runtime/this-firefox
```

3. Click **Load Temporary Add-on**.
4. Select the extension's `manifest.json` file.
5. The extension should now appear in Waterfox.


## How to Run

1. Start the backend by double-clicking:

```txt
start_backend.bat
```

2. Open the Firefox or Waterfox extension upload page.

3. Upload a scanned or image-based PDF.

4. Wait for OCR processing to finish.

5. Download the searchable PDF output.

## Requirements

* Windows
* Firefox or Waterfox
* Python backend packaged with the project
* Tesseract OCR included or installed locally

## Privacy

Local PDF OCR processes files on your own computer. PDFs are not uploaded to a remote server or cloud OCR service.

## Notes

This project is currently a prototype and may not handle every PDF perfectly. OCR quality depends on the original document quality, image resolution, text size, contrast, and layout complexity.

