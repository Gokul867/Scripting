import PyPDF2 as pdf

with open('dummy.pdf', 'rb')as file:  # rb - read binary
    reader = pdf.PdfFileReader(file)
    print(reader.numPages)  # to get number of pages
    page = reader.getPage(0)  # getting 1st page
    page.rotateCounterClockwise(90)

    writer = pdf.PdfFileWriter()
    # This is stored in memory not updated in original pdf
    writer.addPage(page)

    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
