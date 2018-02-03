def USBdecode(f):
    dict  = {
            #"00":"",

            "04":"a",
            "05":"b",
            "06":"c",
            "07":"d",
            "08":"e",
            "09":"f",
            "0a":"g",
            "0b":"h",
            "0c":"i",
            "0d":"j",
            "0e":"k",
            "0f":"l",
            "10":"m",
            "11":"n",
            "12":"o",
            "13":"p",
            "14":"q",
            "15":"r",
            "16":"s",
            "17":"t",
            "18":"u",
            "19":"v",
            "1a":"w",
            "1b":"x",
            "1c":"y",
            "1d":"z",
            "1e":"1",
            "1f":"2",
            "20":"3",
            "21":"4",
            "22":"5",
            "23":"6",
            "24":"7",
            "25":"8",
            "26":"9",
            "27":"0",
            "28":"\n",
            "2a":"<delete>",
            "2b":"<tab>",
            "2c":" ",
            "2d":"-",
            "2e":"=",
            "2f":"{",
            "30":"}",
            "37":".",
            "38":"/",
            "4f":"<right key>",
            "50":"<left key>"
            }

    flag = []
    lines = f.read().split("\n")
    carsol = 0

    for line in lines:
        if line[4:6] in dict:
            # delete key
            if line[4:6] == "2a":
               flag.pop(carsol-1)
               carsol = carsol - 1
            
            #tab key
            elif line[4:6] == "2b":
               flag.insert(carsol, "\t")
               carsol = carsol + 1

            #right key
            elif line[4:6] == "4f":
                carsol = carsol + 1
            
            #left key
            elif line[4:6] == "50":
                carsol = carsol - 1

            else: 
                if line[0:2] == "02":
                    if line[4:6] == "1e":
                        flag.insert(carsol,"!")
                    else:
                        flag.insert(carsol, dict[line[4:6]].upper())
                else:
                    flag.insert(carsol, dict[line[4:6]])
                carsol = carsol + 1
        

    return "".join(flag)

def main():
    with open('capture') as file:
        flag = USBdecode(file)
        print(flag)

main()
