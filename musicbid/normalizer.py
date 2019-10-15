#python3
import codecs
import re

def create_fixes():
    path = r'spelling_fixes'
    with codecs.open(path, 'r', encoding='utf-8') as f:
        text = f.read().split('\n')
    fixes = []
    for x in text:
        pair = x.split('\t')
        fixes.append((pair[0], pair[1]))
    return fixes


def fix_spelling(text, fixes):
    """Fix spelling case insensitive errors"""

    for fix in fixes:
        # Original Text.
        pattern = fr'\b{fix[0]}\b'
        text = re.sub(pattern, fix[1], text)

        # Capitalize.
        pattern = fr'\b{fix[0].capitalize()}\b'
        text = re.sub(pattern, fix[1].capitalize(), text)

        # Lower.
        pattern = fr'\b{fix[0].lower()}\b'
        text = re.sub(pattern, fix[1].lower(), text)

        # Upper.
        pattern = fr'\b{fix[0].upper()}\b'
        text = re.sub(pattern, fix[1].upper(), text)

        # Title.
        pattern = fr'\b{fix[0].title()}\b'
        text = re.sub(pattern, fix[1].title(), text)
    return text


def normalize_file():
    path = r'C:data.txt'
    out_path = r'norm_data.tsv'

    with codecs.open(path, 'r', encoding='utf-8') as f:
        text = f.read().split('\n')

    export_text = ''

    for line in text:
        normalized_text = fix_spelling(line, fixes)
        if line == normalized_text:
            tag = 'no_change'
        elif line != normalized_text:
            tag = 'change'
        export_text += f'{line}\t{normalized_text}\t{tag}\n'

    with codecs.open(out_path, 'w', encoding='utf-8') as f:
        f.write(export_text)

# Preliminary eyeball test to make sure results are looking ok.
s = [
    'BBb Contra Clarinet Selmer 41',
    'Bb Clarnet',
    'Bb CLARNET',
    'Bbb Tuba',
    'Trumpet, B-Flat, Standard, with Case King 601',
    'Bass Clarinet w/ case, Selmer, 1430LP',
    'Euphonium 4/4 Soloist model euphonim, 4 valve King 2280SP silver',
    'Saxophone, Alto, E-Flat, Standard, with Case Selmer A5500',
    'Buffet BC2541-5-0 Prodige Student Clarin',
    'La Blanc L7168 Bass Clarinets',
    'CLARINET, CONTRA-ALTO KEY OF EE FLAT . '
    'Yamaha YBB-105WC Series 3-Valve 3/4 BBb Tuba (461352)'
    ]
fixes = create_fixes()
for x in s:
    print(fix_spelling(x, fixes))
