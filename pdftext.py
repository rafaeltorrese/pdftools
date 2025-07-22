import os
import textract
from data import pathtofile

file_list = os.listdir(os.path.join(*pathtofile))

for file in file_list:
    base_file, ext_file = os.path.splitext(file)
    if ext_file == '.pdf':
        path_file = os.path.join(*pathtofile, file)
        text_bytes = textract.process(path_file)
        text = text_bytes.decode('utf-8')
        with open(f'{base_file}.txt', mode='w', encoding='utf-8', newline='') as file:
            file.write(text)