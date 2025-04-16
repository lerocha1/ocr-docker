import os
from pdf2image import convert_from_path
import pytesseract
import fitz

def extrarir_texto_pdf(path):
    doc = fitz.open(path)
    texto = ""
    for page in doc:
        texto += page.get_text()
    return texto

def extrair_texto_ocr(path):
    imagens = convert_from_path(path)
    texto = ""
    for img in imagens:
        texto += pytesseract.image_to_string(img, lang='por')
    return texto

def ler_pdf(path):
    texto = extrarir_texto_pdf(path)
    if texto.strip():
        print("Texto extaíddo do PDF com sucesso.")
        return texto
    else:
        print("Texto extaíddo com OCR com sucesso.")
        return extrair_texto_ocr(path)
    
if __name__ == "__main__":
    arquivo_pdf = "BMB-DC-011.163 - Emenda à inicial (ad5cd6f3-2bff-47f5-9639-ac0a82d5ada7_id_4142).pdf"  
    resultado = ler_pdf(arquivo_pdf)
    print("Resultado:")
    print(resultado)