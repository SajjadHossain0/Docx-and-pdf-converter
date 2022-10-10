from docx2pdf import convert
from pdf2docx import parse
from tkinter.filedialog import *
print("Choose an option...")
print("1. Docx to PDF")
print("2. PDF to Docx\n")
op = int(input("Option : "))
if op == 1:
    input_docx = askopenfilename()
    output_pdf = input("Give us pdf file name : ") + ".pdf"
    convert(input_docx, output_pdf)
elif op == 2:
    input_pdf = askopenfilename()
    output_docx = input("Give us docx file name : ") + ".docx"
    parse(input_pdf, output_docx)
else:
    print("Invalid input!")