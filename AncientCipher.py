Answer = ''
for X in range (3, 21):
    for A in range (1, 20):
        if A >= X:
            break
        for B in range (1, 20):
            if B >= A:
                break
            if X % (A + B) == 0:
               Answer = Answer + str(A) + str(B)
    if X < 10:
        print (f''' ::{X}:: {Answer}- the password !! ''')
    else:
        print(f''' :{X}:: {Answer}- the password !! ''')

