# Ressl MCP Assignment

This project implements a basic **MCP (Model-Command-Prompt) Server** and **Client** that enables:

- Uploading files via a web UI
- Editing files via prompt-based commands (`uppercase`, `append`, `replace`)
- Deleting files with a filename input

---

## 🔧 Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML + JS
- **Server**: Uvicorn

---

## 📂 Folder Structure

ressl-mcp-assignment/
├── main.py # FastAPI server
├── index.html # Frontend
├── uploaded_files/ # Stores uploaded .txt files
└── README.md # This file


---

## 🚀 How to Run the Project

### 1. Clone the Repo

```bash
git clone https://github.com/Lavanyaraju19/ressl-mcp-assignment.git
cd ressl-mcp-assignment

2. Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # Mac/Linux

3. Install FastAPI & Uvicorn

pip install fastapi uvicorn python-multipart

4. Start the Server

uvicorn main:app --reload
The server runs at: http://127.0.0.1:8000


8000

🌐 Using the Frontend
1.Open index.html in your browser (Chrome/Edge)

2.Upload a .txt file

3.Use the edit prompt with:

  uppercase

  append

  replace

4.Use delete input to remove the file

✅ Example Commands
Upload → test.txt uploaded.

Edit (uppercase) → File becomes ALL CAPS

Delete → test.txt deleted

🧪 Test Cases
Upload test.txt

Edit with prompt: uppercase

Delete file: test.txt

Verify changes in /uploaded_files/ folder

📸 Submission
This repo is created for the technical assignment for Ressl.ai.
A screen recording demonstrating upload, edit, and delete will accompany this submission.

✨ Author
Lavanya J Raju
GitHub: @Lavanyaraju19

