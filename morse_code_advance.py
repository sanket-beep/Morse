from itertools import groupby

MORSE_CODE = { '.-':'A', '-...':'B',
'-.-.':'C', '-..':'D', '.':'E',
'..-.':'F', '--.':'G', '....':'H',
'..':'I', '.---':'J', '-.-':'K',
'.-..':'L', '--':'M', '-.':'N',
'---':'O', '.--.':'P', '--.-':'Q',
'.-.':'R', '...':'S', '-':'T',
'..-':'U', '...-':'V', '.--':'W',
'-..-':'X', '-.--':'Y', '--..':'Z',
'.----':'1', '..---':'2', '...--':'3',
'....-':'4', '.....':'5', '-....':'6',
'--...':'7', '---..':'8', '----.':'9',
'-----':'0', '--..--':',', '.-.-.-':'.',
'..--..':'?', '-..-.':'/', '-....-':'-',
'-.--.':'(', '-.--.-':')'}  

def decodeBitsAdvanced(bits):
    bits = bits.strip("0")
    if not bits: return ""

    minall = min(len(list(g)) for b, g in groupby(bits))
    maxone = max(len(list(g)) for b, g in groupby(bits) if b == "1")
    dashlen = maxone if maxone != minall else minall * 3
    
    normalized = "".join([
        b * (1 if len(g) < (minall + dashlen) / 2.0
        else 3 if len(g) <= dashlen + 2 else 7)
        for b, g in ((b, list(g)) for b, g in groupby(bits))])

    return decodeMorse((normalized.replace('0000000', '   ')
                      .replace('111', '-')
                      .replace('000', ' ')
                      .replace('1', '.')
                      .replace('0', '')))


def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

def encodeMorse(sentence):
  sentence = sentence.upper()
  morse = ''
  key_list = list(MORSE_CODE.keys()) 
  val_list = list(MORSE_CODE.values()) 
  for character in sentence:
    space = 0
    if character == ' ':
      morse += '  '
      continue
    index = key_list[val_list.index(character)]
    morse += index + ' '
  return morse

def encode_to_bits(sentance):
  morseCode = encodeMorse(sentance)
  bits = morseCode.replace('   ','0000000').replace(' ','000').replace('-', '1110').replace('.','10')
  return bits