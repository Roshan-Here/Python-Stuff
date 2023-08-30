from docx import Document
from docx.shared import Pt # for font sizing...

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
k.font.size = Pt(25)
# run.style = 'Emphasis'


d.save("wow.docx")