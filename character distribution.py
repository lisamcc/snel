import random

def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)

    return text

def mean(counts):
    pass

    return 0

def chi_sqaure(counts):
    expected = mean(counts)

    X = 0

    for n in counts:
        pass

    return X

content = generate_random_text(100)

with open('new_file.txt', 'w') as f:
    f.write(content)
    

