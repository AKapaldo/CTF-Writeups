from functools import reduce

shares = {i+1:int(l,16) for i,l in enumerate(open("cats.txt")) if l.strip()}
p = int("010000000000000000000000000000000000000000000000000000000000000129",16)
modinv = lambda a,p: pow(a,-1,p)

secret = sum(y * reduce(lambda x,j:x*-j%p,(j for j in shares if j!=i),1) * modinv(reduce(lambda x,j:x*(i-j)%p,(j for j in shares if j!=i),1),p) for i,y in shares.items()) % p
print(hex(secret), secret.to_bytes((secret.bit_length()+7)//8,"big"))
