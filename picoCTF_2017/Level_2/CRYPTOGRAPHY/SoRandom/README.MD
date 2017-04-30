# picoCTF 2017: SoRandom

**Level:** 2 **Category:** CRYPTOGRAPHY **Point:** 75 

**Description:**

>We found [sorandom.py](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_2/CRYPTOGRAPHY/SoRandom/sorandom.py) running at shell2017.picoctf.com:33123. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?
Update (text only) 16:16 EST 1 Apr Running python 2 (same version as on the server)

**Hint:**

>How random can computers be?

## Write-up

Firstly using `nc` connect to the server, we get the randomized flag:

``` 
root@kali:~# nc shell2017.picoctf.com 33123
Unguessably Randomized Flag: BNZQ:2m8807395d9os2156v70qu84sy1w2i6e
```

Then open the sorandom.py, just change the `+random.randrange` to `-random.randrange`, and change the flag into `BNZQ:2m8807395d9os2156v70qu84sy1w2i6e` . Run the [script](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_2/CRYPTOGRAPHY/SoRandom/unrandom.py), we get the flag.

The flag is `9b6098160b2ca5139c83fe29fd7c9e5d`.

PS:This script can't get the correct flag with Windows system. It may because that `you are seeding the Mersenne twister with a string, which is the same as seeding it with the hash of that string, and strings may be subject to hash randomization depending on configuration.`(Thanks to the answerer Sven Marnach at Stack OverFlow).