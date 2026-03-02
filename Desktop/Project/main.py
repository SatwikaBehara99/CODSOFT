from fastapi import FastAPI, UploadFile, File 
import pdfplumber 
import re 
import io 
app = FastAPI() 
@app.get("/") 
def home(): 
    return {"message": "Server Running"}
@app.post("/upload")
async def upload_file(resume: UploadFile = File(...)):

    content = await resume.read()

    print("File received:", resume.filename)
    print("File size:", len(content))

    text = ""

    # If PDF
    if resume.filename.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

    # Extract Email
    email_match = re.search(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    email = email_match.group(0) if email_match else None

    # Extract Phone
    phone_match = re.search(r"\b\d{10}\b", text)
    phone = phone_match.group(0) if phone_match else None

    # Extract Name (Simple assumption: first line)
    lines = text.split("\n")
    name = lines[0] if lines else None

    return {
        "name": name,
        "email": email,
        "phone": phone
    }