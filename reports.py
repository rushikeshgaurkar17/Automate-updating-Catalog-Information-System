#!/usr/bin/env python3

from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
  styles = getSampleStyleSheet()
  rep = SimpleDocTemplate(file)
  rt = Paragraph(title, styles['h1'])
  ri = Paragraph(add_info, styles['BodyText'])
  el =  Spacer(1,20)

  rep.build([rt, el, ri, el])
