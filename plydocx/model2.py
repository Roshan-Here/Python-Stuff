from docx import Document
from docx.shared import Pt,Inches # for font sizing...
from docx.enum.text import WD_UNDERLINE
from docx.shared import RGBColor # for font color setting....
from docx.enum.dml import MSO_THEME_COLOR #MSO theme selector color
from docx.enum.text import WD_ALIGN_PARAGRAPH # alignmennt
from docx.enum.style import WD_STYLE
from functions import insertHR,add_hyperlink,fff
from docx.enum.text import WD_LINE_SPACING # line spacing


d = Document()
def paara(spacing=False,Bbullet=False):
    para = d.add_paragraph('')
    if spacing == True:
        para.paragraph_format.space_before = Pt(1)
        para.paragraph_format.space_after = Pt(1)
        para.paragraph_format.line_spacing = Pt(10)
    if Bbullet == 1:
        para.style = 'List Bullet'
    return para


#####################
# Header Section
#####################

# headding-1
section = d.sections[0]  # Get the first section of the document
section.left_margin = Inches(.5)  # Set the left margin to 1 inch
section.right_margin = Inches(.5)  # Set the right margin to 1 inch
section.top_margin = Inches(.5)   # Set the top margin to 1 inch
section.bottom_margin = Inches(.5)

sections = d.sections[0] # first_page section
header = sections.header
para = header.add_paragraph('')
para.alignment = WD_ALIGN_PARAGRAPH.CENTER
l = para.add_run('Muhammed Roshan P S')
l.bold = True
l.font.size = Pt(19)
l.font.name = 'PT Serif'
l.font.color.theme_color = MSO_THEME_COLOR.DARK_1
# l.font.underline = True


# sections = d.sections[0]  # Get the first section of the document
# header = section.header
nxt = header.add_paragraph("")
nxt.alignment = WD_ALIGN_PARAGRAPH.CENTER
add_hyperlink(nxt, url='http://mailto:muhammedroshanps@gmail.com', text=' muhammedroshanps@gmail.com |',color='2b3137',underline=True)
add_hyperlink(nxt, url='https://github.com/Roshan-Here', text='Github |',color='24292e',underline=True)
add_hyperlink(nxt, url='https://www.linkedin.com/in/muhammed-roshan-ps/', text=' Linkdin |',color='0A66C2',underline=True)
add_hyperlink(nxt, url='http://tel:9809031477', text=' +919809031477',color='5B51D8',underline=True)
# nxt.font.name = 'PT Serif'
# nxt.font.size = Pt(11)
insertHR(nxt,fontsize='20',typee='thick')

###############
#main_body
###############

para = d.add_heading('',level=5)
l = para.add_run('Summary')
l.font.size = Pt(11)
l.font.name = 'PT Serif'
l.bold = True
l.font.color.theme_color = MSO_THEME_COLOR.DARK_1 

para = paara(spacing=True)
j = para.add_run('Financial Advisor with 7+ years of experience delivering financial/investment advisory services to high value clients. Proven success in managing multi-million dollar portfolios, driving profitability, and increasing ROI through skillful strategic planning, consulting, and financial advisory services.')
# para.paragraph_format.line_spacing = Pt(1)
fff(j,size=int(10),fntname='PT Serif')

#heading -2
para = d.add_heading('',level=5)
j = para.add_run('Professional Experience')
fff(j,size=int(11),fntname='PT Serif',bbold=True)


para = paara(spacing=True)
j = para.add_run('Month YYYY-Present')
para.alignment =  WD_ALIGN_PARAGRAPH.RIGHT
fff(j,size=int(10),fntname='PT Serif',iitalic=True)


para = paara()
j = para.add_run('Job Heading')
fff(j,size=int(10),fntname='PT Serif',bbold=True)




d.save('nice.docx')