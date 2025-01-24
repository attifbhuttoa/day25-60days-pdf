from fpdf import FPDF
import glob
from pathlib import Path

filepath = glob.glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")


for file in filepath:
    pdf.add_page()
    file_name = Path(file).stem
    name = file_name.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, txt=f"{name}", ln=1)
    pdf.set_font(family="Times", size=10)

    with open(file, "r") as text:
        content = text.read()
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=6, txt=content)




pdf.output("all.pdf")











