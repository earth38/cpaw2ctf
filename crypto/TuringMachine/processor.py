def encrypt(s):
    tape = s   
    tape = list(tape)

    for i in range(len(tape)):
        tape[i] = format(ord(tape[i]),"b")
        while len(tape[i]) != 8:
            tape[i] = "0" + tape[i]
    tape = "".join(tape)
    tape = list(tape)

    q = 0
    for i in range(len(tape)):
        if q == 0:
            if tape[i] == "0":
                #deleted
                pass
            elif tape[i] == "1":
                #deleted
                q = 1
        elif q == 1:
            if tape[i] == "1":
                #deleted
                if tape[i+1] == "1":
                    break
                else:
                    pass
            elif tape[i] == "0":
                #deleted
                if tape[i+1] == "0":
                    break
                else:
                    pass
       
    return(tape)    

def nextCharacter(candidate):
    if candidate == "Z":
        candidate = "a"
    elif candidate == "z":
        candidate = "0"
    elif candidate == "9":
        candidate = "A"
    else:
        candidate = chr(ord(candidate)+1)

    return(candidate)

def changeCharacter(s,i):
    s_list = list(s)
    s_list[i] = nextCharacter(s_list[i])
    return "".join(s_list)
    

def main():
    candidate = "A"*7

    for s0 in range(62):
        for s1 in range(62):    
            for s2 in range(62):    
                for s3 in range(62):    
                    for s4 in range(62):    
                        for s5 in range(62):    
                            for s6 in range(62):    
                                if encrypt(candidate) == "00001110110001101100111011001101110010011100110111001100":
                                    print candidate
                                    exit()
                                
                                candidate = changeCharacter(candidate,6)
                                if candidate[6] == "A":
                                    break
                                print candidate

                            candidate = changeCharacter(candidate,5)
                            if candidate[5] == "A":
                                break

                        candidate = changeCharacter(candidate,4)
                        if candidate[4] == "A":
                            break

                    candidate = changeCharacter(candidate,3)
                    if candidate[3] == "A":
                        break

                candidate = changeCharacter(candidate,2)
                if candidate[2] == "A":
                    break

            candidate = changeCharacter(candidate,1)
            if candidate[1] == "A":
                break


        candidate = changeCharacter(candidate,0)
        if candidate[0] == "A":
            break


main()
