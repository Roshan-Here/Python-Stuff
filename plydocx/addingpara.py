from docx import Document
from docx.shared import Pt # for font sizing...
from docx.enum.text import WD_UNDERLINE
from docx.shared import RGBColor # for font color setting....

d = Document()

d.add_heading("adding para",level=0)

para = d.add_paragraph()
# bold para
para.add_run('wow its nice').bold = True
# italic para on same stanzzza
para.add_run(' oopz').italic = True

paragraph = d.add_paragraph('Normal text, ')
run = paragraph.add_run('text with emphasis.' ,'Emphasis')
j = para.add_run(' check ', 'Strong')
# added font name
k = para.add_run('its a Subtle Reference check how i look', 'Subtle Reference')
k.font.name = 'Times New Roman'
# font sizing
k.font.size = Pt(25)
# font underline
k.font.underline = True
# dotted underline | different types (https://python-docx.readthedocs.io/en/latest/api/enum/WdUnderline.html#wd-underline)
j.font.underline = WD_UNDERLINE.DOT_DASH
j.font.color.rgb = RGBColor(142, 131, 88)

d.save("wow.docx")