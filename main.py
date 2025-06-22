from fastapi import FastAPI, UploadFile, File, Form
import os

app = FastAPI()
UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Root test route (you can add this here)
@app.get("/")
def read_root():
    return {"message": "Hello, Ressl!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": f"{file.filename} uploaded."}

@app.post("/edit/")
def edit_file(filename: str = Form(...), instruction: str = Form(...)):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(path):
        return {"error": "File not found"}

    with open(path, "r+", encoding="utf-8") as f:
        content = f.read()
        if "uppercase" in instruction.lower():
            content = content.upper()
        elif "append" in instruction.lower():
            content += "\nAppended by MCP Server"
        else:
            content = content.replace("old", "new")
        f.seek(0)
        f.write(content)
        f.truncate()

    return {"message": "File edited."}

@app.post("/delete/")
def delete_file(filename: str = Form(...)):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)
        return {"message": f"{filename} deleted"}
    return {"error": "File not found"}
