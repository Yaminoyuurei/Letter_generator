import datetime
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from module.Person import Person
from docx.shared import Cm

document = Document()
sections = document.sections
for section in sections:
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(3)
    section.left_margin = Cm(3)
    section.right_margin = Cm(3)

obj = ""   
expediteur = Person("NOM","PRÉNOM","ADRESSE","CP","VILLE")
destinataire = Person("NOM","PRÉNOM","ADRESSE","CP","VILLE")

p_expediteur = document.add_paragraph(expediteur.check())   

p_destinataire =document.add_paragraph(destinataire.check())
p_destinataire.alignment= WD_ALIGN_PARAGRAPH.RIGHT

p_lieu = document.add_paragraph(f"{expediteur.ville}, le {datetime.datetime.now().strftime('%d/%m/%Y')}")
p_lieu.alignment= WD_ALIGN_PARAGRAPH.RIGHT

if obj != "":
    p_objet = document.add_paragraph(f"Objet : {obj}")

p_appel = document.add_paragraph(f"Madame, Monsieur,\n\n")
p_core = document.add_paragraph("fdgheomudhgfeoghpoejgf fgrgpergperogjerzigùerjg iregskjrjighroighrs orh^qhiurhtoqjheijfqj ffhrlhgrghrghrlg hrlgql \n dfoihdoig hjroigjrpigjrp igj^phijtph rjdfghrthte grgergrge \n rfgrrgerrhgtgdgrtgrgreg \n hrhhtrtrhthdfthth rhdfhthytrh tfdhtrht")

p_signature = document.add_paragraph(f"{expediteur.prenom} {expediteur.nom}")
p_signature.alignment= WD_ALIGN_PARAGRAPH.RIGHT
document.save('test.docx')