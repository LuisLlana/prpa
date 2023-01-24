

def code_letter_atbash(c):
    if 'a' <= c and c <= 'z':
          result = chr(ord('z')-(ord(c)-ord('a')))
    elif 'A' <= c and c <= 'Z':
          result = chr(ord('Z')-(ord(c)-ord('A')))
    else:
          result = c
    return result

def coder_atbash(message):
    result = ''
    for c in message:
        result = result + code_letter_atbash(c)
    return result

def decoder_atbash(message):
    return coder_atbash(message)

def decoder_transposition(message):
    result = ''
    med = len(message)//2 + len(message)%2
    for i in range(med-1):
         result = result + message[i]+message[med+i]
    result = result + message[med-1]
    if len(message)%2 ==0:
       result = result + message[len(message)-1]
    return result

def coder_transposition(message):
    result = ''
    for i in range(0,len(message),2):
        result = result + message[i]
    for i in range(1,len(message),2):
        result = result + message[i]
    return result
