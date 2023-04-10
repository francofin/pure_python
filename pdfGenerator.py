from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
data = pd.read_csv("topics.csv",sep=",")
for idx, row in data.iterrows():
    for i in range(row['Pages']):
        pdf.add_page()
        pdf.set_font(family="Helvetica", style="B", size=12)
        pdf.set_text_color(78,78, 78)
        pdf.cell(w=0, h=12, txt=f"{row['Order']}. {row['Topic']}", align="L", ln=1)
        pdf.line(10,22,200,22)
        for j in range(30, 260, 10):
            pdf.line(10, j, 200, j)
        pdf.ln(255)
        pdf.set_font('Helvetica', style="I", size=10)
        pdf.set_text_color(26, 157, 84)
        pdf.cell(w=0, h=10, txt =f"{row['Topic']}...{idx+i}", align="R")
        # pdf.footer()
pdf.output("Output.pdf")

# pdf.add_page()
#
#
# pdf.cell(w=0, h=12, txt="Page Content", align="L",ln=1,  border=1)
#
# pdf.add_page()
# pdf.set_font(family="Helvetica", size=12)
# pdf.cell(w=0, h=12, txt="Page One", align="L",ln=1, border=1)
# pdf.cell(w=0, h=12, txt="Page Content", align="L",ln=1,  border=1)
#
