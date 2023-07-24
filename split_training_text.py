import os
import random
import pathlib
import subprocess

training_text_file = 'langdata/eng.training_text'
fontconf_dir = '/'
xsize = 4000
ysize = 700
font = ""
lines = []

with open(training_text_file, 'r') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

output_directory = 'tesstrain/data/RedHatMono-ground-truth'

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

random.shuffle(lines)

count = 32020

lines = lines[:count]

line_count = 0
for line in lines:
    training_text_file_name = pathlib.Path(training_text_file).stem
    line_training_text = os.path.join(output_directory, f'{training_text_file_name}_{line_count}.gt.txt')
    with open(line_training_text, 'w') as output_file:
        output_file.writelines([line])

    file_base_name = f'eng_{line_count}'

    ln = os.system(f'text2image --text={line_training_text} --outputbase={output_directory}/{file_base_name} --max_pages=1 --strip_unrenderable_words --leading=32 --xsize={xsize} --ysize={ysize} --char_spacing=1.0 --exposure=0 --unicharset_file=langdata/eng.unicharset --fontconfig_tmpdir={fontconf_dir} --font="{font}" 2>/dev/null')
    if ln == 0:
        print(f'successfully created: eng_{line_count}.tif')
        print(f'successfully created: eng_{line_count}.gt.txt')
        print(f'successfully created: eng_{line_count}.box')
    else:
        print('NOT ENOUGH DATA')
    line_count += 1
