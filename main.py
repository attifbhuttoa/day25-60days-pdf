import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# create file path to access the excel files
filepaths = glob.glob("invoices/*.xlsx")

# iterrate over all the excel files
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
#     create pdf object
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # add page
    pdf.add_page()
    # extract the file name
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    # set-font
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, txt=f"Invoice number {invoice_nr}")
    pdf.output(f"pdf/{filename}.pdf")


