import docx
from docx import Document
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn
from docx.enum.dml import MSO_THEME_COLOR 
from docx.shared import Pt

###############################################
# https://github.com/python-openxml/python-docx/issues/105#issuecomment-442786431
##############################################

def insertHR(paragraph,fontsize='6',color='black',typee='double'):
    p = paragraph._p  # p is the <w:p> XML element
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    pPr.insert_element_before(pBdr,
        'w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap',
        'w:overflowPunct', 'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
        'w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind',
        'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
        'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap',
        'w:outlineLvl', 'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr',
        'w:pPrChange'
    )
    bottom = OxmlElement('w:bottom') #top
    bottom.set(qn('w:val'), typee) #double , #doubleWave ,#triple ,#threeDEmboss, #threeDEngrave, #thickThinSmallGap, #thinThickLargeGap, #thinThickMediumGap
    bottom.set(qn('w:sz'), fontsize) #helps to assign line width 
    bottom.set(qn('w:space'), '2')
    bottom.set(qn('w:color'), color)
    pBdr.append(bottom)

#############################################
#############################################




###############################
# https://stackoverflow.com/questions/47666642/adding-an-hyperlink-in-msword-by-using-python-docx
# https://github.com/python-openxml/python-docx/issues/74#issuecomment-244602378
################################

def add_hyperlink(paragraph, url, text, color, underline):
    """
    A function that places a hyperlink within a paragraph object.

    :param paragraph: The paragraph we are adding the hyperlink to.
    :param url: A string containing the required url
    :param text: The text displayed for the url
    :color: required font color in RGB format
    :return: The hyperlink object
    """

    # This gets access to the document.xml.rels file and gets a new relation id value
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    # Create a w:r element
    new_run = docx.oxml.shared.OxmlElement('w:r')

    # Create a new w:rPr element
    rPr = docx.oxml.shared.OxmlElement('w:rPr')
    # rFonts = rFonts = rPr.get_or_add_rFonts()

    # Add color if it is given
    if not color is None:
      c = docx.oxml.shared.OxmlElement('w:color')
      c.set(docx.oxml.shared.qn('w:val'), color)
      rPr.append(c)

    # Remove underlining if it is requested
    if not underline:
      u = docx.oxml.shared.OxmlElement('w:u')
      u.set(docx.oxml.shared.qn('w:val'), 'none')
      rPr.append(u)

    # rFonts.set(qn('w:cs'),ffname)
    # rPr.append(rFonts)
# <w:rFonts
    # if ffname !=None:
      # u = docx.oxml.shared.OxmlElement('w:rFonts')
      # u.set(docx.oxml.shared.qn('w:cs'), ffname)


    # Join all the xml elements together add add the required text to the w:r element
    new_run.append(rPr)
    new_run.text = text

    hyperlink.append(new_run)

    paragraph._p.append(hyperlink)

    return hyperlink


###########################################
########### SETUP FONT | SIZE | BOLD/ITALIC | 
##########################################
def fff(dname,size=int(11),Rrgb=None,theme=MSO_THEME_COLOR.DARK_1,fntname='Open Sans',bbold=False,iitalic=False):
    dname.font.size = Pt(size)
    if Rrgb != None:
        dname.font.color.rgb = Rrgb
    else:
        dname.font.color.theme_color = theme
    if bbold == True:
        dname.bold = True
    else:
        pass
    if iitalic == 1:
        dname.italic = True
    else:
        pass
    dname.font.name = fntname
