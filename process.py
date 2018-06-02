sample_file = open('sample.cpp')
sample_code = ''.join(list(sample_file))

import os

def process_color_theme(theme):
    header = '#define THEME "%s"\n\n//////////////////////\n'
    header_str = header % theme
    f = open('sample-' + theme + '.cpp', 'w')
    f.write(header_str)
    f.write(sample_code)
    f.close()
    command = 'highlight -O rtf -k manaco -K 15 -s %s sample-%s.cpp > themes/%s-sample.rtf'
    os.system(command % (theme, theme, theme))

if __name__ == "__main__":
    color_file_name = r'highlight-w.output'
    for theme in open(color_file_name):
        process_color_theme(theme[:-1])
