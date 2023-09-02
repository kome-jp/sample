# Caesar cipher:Encryption & Decryption
def Caesar_cipher(value, shift = 3, mode = "Encryption"):
    con_str = ""
    if mode == "Decryption": shift = -shift 
    for i in range(len(value)):  # To judge each character
        code_point = ord(value[i]) 
        if value[i].isupper(): 
            code_point = (code_point - 65 + shift) % 26 + 65 # A:65 
            con_str = con_str + chr(code_point)
        elif value[i].islower():
            code_point = (code_point - 97 + shift) % 26 + 97 # a:97
            con_str = con_str + chr(code_point)
        else:
            con_str = con_str + value[i]
    return con_str

value = "Khoor_Zruog"
mode="Decryption"  # Encryption or Decryption
shift = 3
conversion_str = Caesar_cipher(value, shift=shift, mode=mode) 
conversion_str