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
https://hexed.it
https://stackoverflow.com/questions/45321665/magic-number-for-google-image-format
https://www.google.com/search?q=webp+magic+number&oq=webp+magic+number&aqs=chrome.0.69i59.3110j0j7&sourceid=chrome&ie=UTF-8



## ======== Hash ========
### EASY HASHY
Ooops, I got carried away and hashed my super-secret password. Now I can't find it again ! Please,
help me ! Here's the hash: 37f62f1363b04df4370753037853fe88
https://crackstation.net
## Answer
7f62f1363b04df4370753037853fe88     md5     trololo



### CONFESSIONS
Noting the darkness of your souls, the Admin, may his name be sanctified, has decided to come to the
aid of your souls in perdition: A confessional is now available within this CTF â›ª You can now
unburden your souls of its heaviest secrets, inevitable sins accumulated during your intrusions on
the so fragile little websites of our platform ðŸ™

I was qust informed that a suspicious individual was seen leaving, who did not remind us of any of
your faces. What dark secret could he have confided? ðŸ•µ We are sure he is of great value, but only
God will know, for our service is inviolable! ðŸ’ªðŸ”’

confessions.crypto.blackfoot.io
## Answer
https://www.youtube.com/watch?v=zxY_GdW6WdY&t=328s
Use Basic Enumeration
https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/graphql
Send Basic Enumeration with postman
https://cloudy-crater-1565.postman.co/workspace/2d48321b-a07a-4ee2-8d15-73a228c203d7/request/13154279-fc3aa0d8-cdcb-4536-95c7-98bdf2abbde6
Send get requestLog to have "requestLog.json"
Use "getHash.py" to have all hash of confession
Use "decryptHash.py" to use all hash to get the flag
# The flag is: "ZOB{plz_d0nt_t3ll_any1}"



## ==== Symmetric ====
### SYM1:
Oh no, I qust lost the IV we use for every encrypted file in our production system... All I have is
a screenshot of one time i encrypted some data with it, but the screenshot got edited by a l337
hacker! Can you help me?

The screenshot is here: /ch3.qpg

Use "useTryEncode.py"
# completeCipher is: 02f374a82db50b23a7d09b88f1d976ddc1cf6db4524aac04e222853969367e0d
# potentialIvRes: h4ppyh4ppya5canB
# potentialCipher 02f374a82db50b23a7d09b88f1d976dd
# now I'm found...


## ======== RSA ========
### RSA1: Warm up
Let's see if you got my class. Download /rsa1.pem, it's a public key.
Now download /rsa1Cipher.txt
The message was encrypted using the "PKCS1 OAEP" algorithm with this public key. Try decrypting it.
Oh yeah - and here's a number that could be useful ;)
p = 11901234461494228310064076121482038286429650089208969229876184007349956782094248940290427800597817633601014470221576037327691902428151823981665392121868907
## Answer
➜  RSA1 git:(master) ✗ python3 decodeCipher.py
[Good job! Next chall: /rsa2ez4me.zip]



### RSA2: ManyKeys
Find the challenge yourself.
