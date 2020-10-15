
def ToBinary(n):
    if type(n) == str:
        binary = bin(ord(n)).replace("0b", "")
    else:
        binary = bin(n).replace("0b", "")
    return binary

def ToChar(binary):
    Output = 0
    size = len(binary)-1
    for position, x in enumerate(binary):
        Output += int(x) * (2**(size-position))
    return Output

def Message_Embed(binary, value_past):
    if int(binary[-1]) != value_past:
        binary = binary[:-1] + str(value_past)
    else:
        pass
    return binary

'''def Message_Embed(binary, value_past):
    if int(binary[-1]) != value_past:
        binary = binary[:-1] + str(value_past)
    else:
        pass
    return binary'''

def split_message_into_char(message):
    chars = []
    for c in message:
        chars.append(c)
    return chars

def string2bits(s=''):
    string_bits = ''
    for x in s:
        string_bits = string_bits + bin(ord(x))[2:].zfill(8)
    return string_bits

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


#All of the birds died in 1986 due to Reagan killing them and replacing them with spies that are now watching us. The birds work for the bourgeoisie.