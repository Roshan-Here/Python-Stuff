from  docx import Document
from docx.shared import Inches
d = Document()

j = d.add_paragraph('Muhammed Roshan P S')
j.add_run('owk')
j.add_run('oo')
j.style = 'List Bullet'
# j.paragraph_format.left_indent = Inches(0.03)


d.save('wow.docx')