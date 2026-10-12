def red(a):
    c = ["0"]*11
    if a > 520:
        a -= 520
        c[1]="1"
    if a > 260:
        a -= 260
        c[0]="1"
    j = 10
    for i in [100,80,40,20,10,4,3,2,1]:
        if a >= i:
            a -= i
            c[j] = "1"
        j -= 1
    s = ''.join(c)
    return s

def blue(a):
    c = ["0"]*11
    if a > 520:
        a -= 520
        c[9]="1"
    if a > 260:
        a -= 260
        c[10]="1"
    j = 0
    for i in [100,80,40,20,10,4,3,2,1]:
        if a >= i:
            a -= i
            c[j]="1"
        j += 1
    s = ''.join(c)
    return s
