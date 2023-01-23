import hashlib
f= open("wordlist.txt","r")
y=open("hashlist.txt","r")
hashList=y.read().split()
passList=f.read().split()
def  isPass(passList,word) :
    for a in passList :
        result = hashlib.md5(a.encode())
        if (word==result.hexdigest()) :
            print(" {} is the hash of {} ".format(word,a))
def main(hashlist) :
    for x in hashlist :
        isPass(passList,x)
main(hashList)


    