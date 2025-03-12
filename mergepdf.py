from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

# Get all PDF files in current directory
files = [file for file in os.listdir() if file.endswith(".pdf")]
if not files:
    print("No PDF files found in the current directory.")
    exit()

# Display available files with numbers
print("Available PDF files:")
for i, file in enumerate(files, 1):
    print(f"{i}. {file}")

# Get user input for file order
try:
    order_input = input("Enter the order of file numbers separated by spaces (e.g., '2 1 3'): ")
    selected_indices = list(map(int, order_input.split()))
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
    exit()

# Validate input numbers
for idx in selected_indices:
    if idx < 1 or idx > len(files):
        print(f"Invalid number: {idx}. Valid numbers are between 1 and {len(files)}.")
        exit()

# Create ordered file list based on user input
ordered_files = [files[idx-1] for idx in selected_indices]

# Merge files in specified order
for pdf in ordered_files:
    merger.append(pdf)

# Save output
merger.write("merged-pdf.pdf")
merger.close()
print(f"PDF files merged successfully as 'merged-pdf.pdf'")