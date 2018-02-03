import base64



def decoded(s1):
    encoded = "CRZANFZSAQ3QMF3XWQTBONSTGMS7I52TKNJBNZTX{}===".format(s1)
    #try:
    return base64.b64decode(encoded).decode("ascii")
    #except:
    #return "{} is not ...".format(s)


def decoded2(s1,s2):
    encoded = "CRZANFZSAQ3QMF3XWQTBONSTGMS7I52TKNJBNZTX2{}{}=".format(s1,s2)
    try:
        return base64.b64decode(encoded).decode("ascii")
    except:
        return "{},{} is not ...".format(s1,s2)

def decoded3(s1,s2,s3):
    encoded = "CRZANFZSAQ3QMF3XWQTBONSTGMS7I52TKNJBNZTX2{}{}{}".format(s1,s2,s3)
    #try:
    return base64.b64decode(encoded)
    #except:
    #return "{},{},{} is not ...".format(s1,s2,s3)

def decoded4(s1,s2,s3,s4):
    encoded = "{}{}{}{}NFZSAQ3QMF3XWQTBONSTGMS7I52TKNJBNZTX2===".format(s1,s2,s3,s4)
    try:
        return base64.b64decode(encoded).decode("ascii")
    except:
        return "{},{},{},{} is not ...".format(s1,s2,s3,s4)





def main():
    #print(base64.b32decode("CRZANFZSAQ3QMF3XWQTBONSTGMS7I52TKNJBNZTX2===="))
    print(base64.b32decode("MPJIUKSRLUERRNW4N3W4OA4KKCTWJJ3TOA4OA74FCRIN5JKYIO4EQCDT6NT3B5XWVEGGJSTTESG7YPER5FCRLLC6QFQ2RJM4FFTMRYBXDGUMJDGMK6GHHUCRIVFG5ZB5ZEIJNWQLDZ66UZMLPMUWSJBE446I5VCRK3CDRRBSXB3BT24MPL6STIJTXALWHU5Q74FCRJOUBD7GMJDPMGHJQAUNXFJEWN2PNIUKNACFZH7CN7HKIVA3IHFWP22FCWMBFGEGP3ZXL5VBEPEOLX7U74FCRIFOQNBPZQ7GN7HKJ4UURZFX45CRLIKWGZ2PKC3I4AJ75MHX6YKFCRLIRTH776Z"))
    return

    candidate = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    for s1 in candidate:
        for s2 in candidate:
            for s3 in candidate:
                for s4 in candidate:
                    print(decoded4(s1,s2,s3,s4))
main()
