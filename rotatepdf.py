# Requires PyPDF2 (pip install pypdf2)
import os, sys

# The first argument is the inputPDF file (required).
# The second argument is the rotation (required).
# The second argument is the output PDF file (optional).
if len(sys.argv) == 4:
    infile = sys.argv[1]
    rotation = sys.argv[2]
    outfile = sys.argv[3]
elif len(sys.argv) == 3:
    infile = sys.argv[1]
    rotation = sys.argv[2]
    (fname,fext) = os.path.splitext(infile)
    outfile = fname + '-rotated' + fext
else:
    print "Usage: " + sys.argv[0] + " <in file> <rotation> [<out file>]"
    exit(1)

from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_in = open(infile,'rb')
pdf_reader = PdfFileReader(pdf_in)
pdf_writer = PdfFileWriter()
for pagenum in range(pdf_reader.numPages):
     page = pdf_reader.getPage(pagenum)
     page.rotateClockwise(int(rotation))
     pdf_writer.addPage(page)
pdf_out = open(outfile, 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
