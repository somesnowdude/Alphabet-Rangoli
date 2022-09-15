import string
def print_rangoli(size):
    # your code goes here
    character = string.ascii_lowercase[:size]
    hasil = ""
    for i in range(size):
        if hasil != "":
            hasil += "-"
        hasil += character[size-i-1]
    for x in range(size):
        if x == 0:
            continue
        if hasil != "":
            hasil += "-"
        hasil += character[x]
    spacing = len(hasil)
    for y in range(size-1):
        character = string.ascii_lowercase[y+1:size]
        baris = ""
        for i in range(size-y-1):
            if baris != "":
                baris += "-"
            baris += character[size-i-2-y]
        for x in range(size-y-1):
            if x == 0:
                continue
            if baris != "":
                baris += "-"
            baris += character[x]
        baris = baris.center(spacing, "-")
        hasil = "{}\n{}".format(baris, hasil)
    k = 0
    p = 0
    for i in range(1, size):
        character = string.ascii_lowercase[i:size]
        character2 = string.ascii_lowercase[i+1:size]
        x = "-".join(list(character2[::-1]))
        if x != "":
            x += "-"
        t = ""
        for y in range(1, 3+p):
            if t == "":
                t += "-"
            else:
                t += "-"
        t += x
        o = "-".join(list(character))
        for y in range(1, 3+p):   
            if o != "":
                o += "-"
        p += 2
        k += 2
        o = "{}{}".format(t, o)
        hasil = "{}\n{}".format(hasil, o)
    print(hasil)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)