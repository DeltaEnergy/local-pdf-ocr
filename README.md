\# Local PDF OCR



Local PDF OCR is a privacy-focused OCR tool for Firefox/Waterfox. It converts scanned or image-based PDFs into searchable PDFs using a local backend. Files are processed on the user's computer and are not uploaded to a cloud service.



\## Features



\- Convert scanned PDFs into searchable PDFs

\- Local OCR processing

\- Browser extension interface

\- FastAPI backend

\- Tesseract OCR engine

\- Works with screenshot-heavy PDFs, receipts, forms, and scanned documents



\## Current Status



This is an early prototype.



Working:

\- Local backend

\- PDF upload

\- OCR text extraction

\- Searchable PDF output

\- Firefox/Waterfox extension upload page



Known limitations:

\- OCR accuracy depends on scan quality

\- Complex layouts, maps, receipts, and tiny screenshot text may be imperfect

\- Backend must be started before using the extension



\## How to Run



1\. Start the backend by double-clicking:



```txt

start\_backend.bat

