import hashlib
cout=0
pass_crak= input("MD5 HASH: ")
filelist= input(" enter file name")
try:
    pass_file = open(filelist,"r")
except:
    print("wrong file name ")
    quit()
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_crak:
        print("passward found")
        print("passward is:",word)
        break
if cout == 0:
    print("password is not in this file")