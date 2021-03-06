# rotatedtext.py
from reportlab.platypus.flowables import Flowable

class verticalText(Flowable):


    def __init__(self, text):
        Flowable.__init__(self)
        self.text = text

    def draw(self):
        canvas = self.canv
        canvas.rotate(90)
        fs = canvas._fontsize
        canvas.translate(1, -fs/1.2)  # canvas._leading?
        canvas.drawString(0, 0, self.text)

    def wrap(self, aW, aH):
        canv = self.canv
        fn, fs = canv._fontname, canv._fontsize
        return canv._leading, 1 + canv.stringWidth(self.text, fn, fs)





# vertical_text_table.py
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
      BaseDocTemplate, Frame, Paragraph, NextPageTemplate,
      PageBreak, PageTemplate, Image, Table, TableStyle, Spacer)
#from rotatedtext import verticalText

document = BaseDocTemplate(
    'Vertical.pdf')

Elements = []

titleFrame_1 = Frame(
    0.5*inch, 0.75*inch, 7*inch, 9*inch, id='col1', showBoundary=0)
titleTemplate_1 = PageTemplate(
    id='OneCol', frames=titleFrame_1)
document.addPageTemplates([titleTemplate_1])

cw = [1.2*inch] + [1*inch]*6
rh = [0.25*inch] + [.6*inch] + [0.25*inch]*7

data = [
    ['Some', 'Reporting', '', 'Data', '', 'Here', ''],
    ['', verticalText('Ve'), verticalText('Text'),
        verticalText('Vertical'), verticalText('Text'),
        verticalText('Vertical'), verticalText('Text')],
    ['Row1', '0', '0', '69', '803', '20751', '11627'],
    ['Row2', '0', '0', '1', '0', '1096', '103'],
    ['Row3', '0', '0', '0', '0', '233', '1'],
    ['Row4', '0', '0', '0', '0', '694', '38'],
    ['Row5', '0', '0', '23', '2', '1319', '2'],
    ['Row6', '0', '0', '0', '0', '0', '0'],
    ['TOTAL', '0', '0', '93', '805', '24093', '11771'],
    ]

ts = [
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('SPAN', (1, 0), (2, 0)),
    ('SPAN', (3, 0), (4, 0)),
    ('SPAN', (5, 0), (6, 0)),
    ('SPAN', (0, 0), (0, 1)),
    ('ALIGN', (0, 0), (-1, 1), 'CENTER'),
    ('ALIGN', (0, 2), (-1, -1), 'RIGHT'),
    ('VALIGN', (0, 0), (-1, -2), 'MIDDLE'),
    ('FONT', (0, 0), (-1, 1), 'Helvetica-Bold', 7, 7),
    ('FONT', (0, 2), (0, -2), 'Helvetica-Bold', 7, 7),
    ('FONT', (1, 2), (-1, -2), 'Helvetica', 7, 7),
    ('FONT', (0, -1), (-1, -1), 'Helvetica-Bold', 8, 8),
    ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
    ('BACKGROUND', (0, -1), (-1, -1), colors.black),
]

t = Table(
    data, style=ts,
    colWidths=cw, rowHeights=rh)

Elements.append(t)
document.build(Elements)