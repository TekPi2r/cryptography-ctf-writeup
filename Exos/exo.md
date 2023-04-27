### BASIC2:
57656c6c20646f6e6520212054686520666c616720666f722074686973206368616c6c656e67652069732074686973206d6573736167652e
## Answer
It is an Hex-encoded string
Hex-decoded string is:
Well done ! The flag for this challenge is this message.



### BASIC3: I accidentally XOR-encrypted this file...
Is there any way you can help me recover it? It's at: /ch2.bmp
And I have a bonus point for you if you explain why it was a bad idea to xor-encrypt *this* file...
## Answer
"Merci les loulous"
Mettre key plus longue que BMP Header / Avec les 00 on peux voir que ça se répéte et trouver la clé / + Supposer début du header 'BM' 'FF FF'(taille du fichier en hex) '00 00'(réservé)



### BASIC4:
Oh no, I was browsing the internet and I accidentally xor-encrypted a very important picture, I'm
not sure how... I panicked and I closed the tab I was on, and now I can't find it again!

I need the picture, and I'll give you a bonus if you can find the tab I was on!

/basic4.webp



## Hash     /       ### EASY HASHY
Ooops, I got carried away and hashed my super-secret password. Now I can't find it again ! Please,
help me ! Here's the hash: 37f62f1363b04df4370753037853fe88
https://crackstation.net
## Answer
7f62f1363b04df4370753037853fe88     md5     trololo



## RSA      /       ### RSA1: Warm up
Let's see if you got my class. Download /rsa1.pem, it's a public key.
Now download /rsa1Cipher.txt
The message was encrypted using the "PKCS1 OAEP" algorithm with this public key. Try decrypting it.
Oh yeah - and here's a number that could be useful ;)
p = 11901234461494228310064076121482038286429650089208969229876184007349956782094248940290427800597817633601014470221576037327691902428151823981665392121868907
## Answer
➜  RSA1 git:(master) ✗ python3 decodeCipher.py
[Good job! Next chall: /rsa2ez4me.zip]

