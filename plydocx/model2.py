from docx import Document
from docx.shared import Pt,Inches # for font sizing...
from docx.enum.text import WD_UNDERLINE
from docx.shared import RGBColor # for font color setting....
from docx.enum.dml import MSO_THEME_COLOR #MSO theme selector color
from docx.enum.text import WD_ALIGN_PARAGRAPH # alignmennt
from docx.enum.style import WD_STYLE
from functions import insertHR,add_hyperlink
from docx.enum.text import WD_LINE_SPACING # line spacing


d = Document()


#####################
# Header Section
#####################


section = d.sections[0]  # Get the first section of the document
section.left_margin = Inches(.5)  # Set the left margin to 1 inch
section.right_margin = Inches(.5)  # Set the right margin to 1 inch
section.top_margin = Inches(.5)   # Set the top margin to 1 inch
section.bottom_margin = Inches(.5)

sections = d.sections[0] # first_page section
header = sections.header
para = header.add_paragraph('')
l = para.add_run('Muhammed Roshan P S', 'Strong')
l.font.size = Pt(28)
l.font.color.theme_color = MSO_THEME_COLOR.DARK_1
# l.font.underline = True


sections = d.sections[0]  # Get the first section of the document
header = section.header
nxt = header.add_paragraph("")
# nxt.alignment = WD_ALIGN_PARAGRAPH.CENTER
add_hyperlink(nxt, url='http://mailto:muhammedroshanps@gmail.com', text=' muhammedroshanps@gmail.com |',color='2b3137',underline=True)
add_hyperlink(nxt, url='https://github.com/Roshan-Here', text='Github |',color='24292e',underline=True)
add_hyperlink(nxt, url='https://www.linkedin.com/in/muhammed-roshan-ps/', text=' Linkdin |',color='0A66C2',underline=True)
add_hyperlink(nxt, url='http://tel:9809031477', text=' +919809031477',color='5B51D8',underline=True)
insertHR(nxt,fontsize='20')




d.save('nice.docx')