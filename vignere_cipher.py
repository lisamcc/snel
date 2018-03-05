#vigenere cipher
def encrypt(message, key):
    encryption = ""
    loc = 0
    for i in range(len(message)):
        
        total = ord(message[loc]) + ord(key[loc])
               
        if total < 32:
            new = 31 - total
            new_value = 126 - new
        
        elif total > 126:
            new = total - 126
            new_value = 31 + new

        else:
            new_value = total
        
        new_letter = chr(new_value)


        encryption += new_letter
        loc +=1
        
    return(encryption)


                   
def key(message):

    key = ""

    for i in range(len(message)):
        if len(key)==0:
            key+="e"
        elif key[-1]=="e":
            key+="n"
        elif key[-1]=="n":
            key+="i"
        elif key[-1]=="i":
            key+="g"
        elif key[-1]=="g":
            key+="m"
        elif key[-1]=="m":
            key+="a"
        elif key[-1]=="a":
            key+="e"

    return key

with open("text_files/file_016499.txt", 'r') as f:
    message = f.read()
print(encrypt(message, key(message)))

