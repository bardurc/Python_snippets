# Script to merge multiple PDFs into one single PDF

from PyPDF2 import PdfFileMerger
import os
# natsort is used to get same sorting as the native OS
from natsort import os_sorted


output_fname = 'ENTER OUTPUT FILENAME'

pdfs = []

# Find all files ending in .pdf
# os.listdir() adds the filenames to a list
for fname in os_sorted(os.listdir()):
    if fname.endswith('.pdf'):
        pdfs.append(fname)

# Invoke pdf merger object
merger = PdfFileMerger()

# Iterate through the filenames and merge pdfs
for pdf in pdfs:
    print(f'Merging {pdf}')
    merger.append(pdf)

print('#'*60)
# Write merged pdf to new file
print('Writing merged pdf')
merger.write(output_fname)
merger.close()
