"""
PDF Merger

This script allows the user to merge multiple PDF files into a single PDF.
"""

from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(pdf_list, output_filename):
    pdf_writer = PdfFileWriter()

    for pdf in pdf_list:
        pdf_reader = PdfFileReader(pdf)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

pdf_files = ['sample1.pdf', 'sample2.pdf']
merge_pdfs(pdf_files, 'merged.pdf')
