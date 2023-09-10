from docx import Document
from docx.shared import Pt,Inches # for font sizing...
from docx.enum.text import WD_UNDERLINE
from docx.shared import RGBColor # for font color setting....
from docx.enum.dml import MSO_THEME_COLOR #MSO theme selector color
from docx.enum.text import WD_ALIGN_PARAGRAPH # alignmennt
from docx.enum.style import WD_STYLE
from functions import insertHR,add_hyperlink


#add a hyperlink with a custom color and no underline
# hyperlink = add_hyperlink(p, 'http://www.google.com', 'Google', 'FF8822', False)


###############################
# https://stackoverflow.com/questions/47666642/adding-an-hyperlink-in-msword-by-using-python-docx
################################

d = Document()


#####################
# Header Section
#####################


section = d.sections[0]  # Get the first section of the document
section.left_margin = Inches(.5)  # Set the left margin to 1 inch
section.right_margin = Inches(.5)  # Set the right margin to 1 inch
section.top_margin = Inches(.5)   # Set the top margin to 1 inch
section.bottom_margin = Inches(.5)

# playing with sections
sections = d.sections[0] # first_page section
header = sections.header
para = header.add_paragraph('')
# para.text = "checking"
# para.font.color.rgb = RGBColor(142, 131, 88)
# para.styles = d.styles["Header"]
para.alignment = WD_ALIGN_PARAGRAPH.CENTER
l = para.add_run('Muhammed Roshan P S', 'Strong')
l.font.size = Pt(24)
l.font.color.theme_color = MSO_THEME_COLOR.DARK_1
l.font.underline = True

sections = d.sections[0]  # Get the first section of the document
header = section.header
nxt = header.add_paragraph("")
nxt.alignment = WD_ALIGN_PARAGRAPH.CENTER
# k = nxt.add_run(' linkdin ')
# k = nxt.add_hyperlink(text='foobar', url='http://github.com')
# add_hyperlink(paragraph, url='http://google.com', text='Google', color=None/'FF8822', underline=True/False):
add_hyperlink(nxt, url='https://github.com/Roshan-Here', text='Github |',color='24292e',underline=True)
add_hyperlink(nxt, url='https://www.linkedin.com/in/muhammed-roshan-ps/', text=' Linkdin |',color='0A66C2',underline=True)
add_hyperlink(nxt, url='http://mailto:muhammedroshanps@gmail.com', text=' muhammedroshanps@gmail.com |',color='2b3137',underline=True)
add_hyperlink(nxt, url='http://tel:9809031477', text=' +919809031477',color='5B51D8',underline=True)
insertHR(nxt,fontsize='20')
# add_hyperlink(nxt, text=' | Instagram ', url='http://google.com')
# add_hyperlink(nxt, text=' | Wiki ', url='http://google.com')
# k.font.size = Pt(10)
# k.font.color.theme_color = MSO_THEME_COLOR.DARK_1


##############################################
# Main Body
##############################################


# p = d.add_heading("adding para",level=0)

para = d.add_paragraph('')
l = para.add_run('TECHNICAL SKILLS')
l.font.size = Pt(12)
l.font.color.theme_color = MSO_THEME_COLOR.ACCENT_1
l.font.name = 'Calibri'
insertHR(para,color='black')
# bold para

para = d.add_paragraph('')
para.add_run('wow its nice').bold = True
# italic para on same stanzzza
para.add_run(' oopz').italic = True


# https://www.resume.com/sample/civil-engineer/

# work --tomorrow | sleep well 


d.save("wow.docx")