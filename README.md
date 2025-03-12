# SequenPDF 📄✨  
**A Smart PDF Merger with Custom Sequencing**  

---

### 🔍 Overview  
SequenPDF is a lightweight Python tool that merges PDF files in **user-defined order** via a simple command-line interface. Unlike basic mergers, it prioritizes **manual sequencing control**, making it ideal for compiling reports, invoices, or documents where page order matters.  

---

### 🚀 Features  
- **Auto-Detect PDFs**: Scans the current directory for PDF files instantly  
- **Interactive Menu**: Displays numbered list of detected files  
- **Custom Order Input**: Merge files in any sequence (e.g., `3 1 2`)  
- **Input Validation**: Guards against invalid/non-existent file numbers  
- **Lightweight**: Minimal dependencies (only `PyPDF2` + native Python modules)  

---

### ⚙️ Installation  
1. **Install Python 3.x**: [Download here](https://www.python.org/downloads/)  
2. **Install PyPDF2**:  
   ```bash  
   pip install PyPDF2  
