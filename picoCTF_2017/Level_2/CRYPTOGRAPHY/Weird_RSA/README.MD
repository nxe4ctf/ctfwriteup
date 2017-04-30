# picoCTF 2017: Weird RSA

**Level:** 2 **Category:** CRYPTOGRAPHY **Point:** 90 

**Description:**

>We recovered some [data](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_2/CRYPTOGRAPHY/SoRandom/RSA.txt). It was labeled as RSA, but what in the world are "dq" and "dp"? Can you decrypt the ciphertext for us?

**Hint:**

## Write-up

The wikipedia of the `RSA`:[https://en.wikipedia.org/wiki/RSA_(cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), read the part of `Using the Chinese remainder algorithm`.

Then using the python [script](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_2/CRYPTOGRAPHY/Weird_RSA/decrypt.py), we get the flag. Tips: Using pow(c,dp,p) instead of using pow(c,dp)%p, the former way computed more efficiently.

The flag is `Theres_more_than_one_way_to_RSA`.