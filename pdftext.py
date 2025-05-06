import textract
from data import pathtofile, toc, chapter_start




for chapter in chapter_names:
    path_file = f'{pathtofile}/{chapter}.pdf'
    text_bytes = textract.process(path_file)
    text = text_bytes.decode('utf-8')
    with open(f'{chapter}.txt', mode='w', encoding='utf-8', newline='') as file:
        file.write(text)