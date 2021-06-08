# Script to split one PDF into multiple PDFs
# Output PDFs each contain one page from the input PDF

from PyPDF2 import PdfFileWriter, PdfFileReader


fname = 'ENTER INPUT FILENAME'

# Open pdf file as binary (rb)
inp = PdfFileReader(open(fname, 'rb'))

# Iterate through all pages in the pdf
for i in range(inp.numPages):
    output = PdfFileWriter()
    # Split pdf in single pages
    output.addPage(inp.getPage(i))
    # Write each page to new file
    # Remember to open output file as binary (wb)
    with open(f'pdf_page_{i}.pdf', 'wb') as outstream:
        output.write(outstream)
