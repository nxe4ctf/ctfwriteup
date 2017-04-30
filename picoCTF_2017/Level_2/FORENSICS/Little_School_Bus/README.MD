# picoCTF 2017: Little School Bus

**Level:** 2 **Category:** FORENSICS **Point:** 75
 
**Description:**

>Can you help me find the data in this [littleschoolbus.bmp](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_2/FORENSICS/Little_School_Bus/littleschoolbus.bmp)?

**Hint:**

>Look at least significant bit encoding!!

## Write-up

LSB encoding, so using the Stegsolve to analyse it.

`Analyse`-`Data Extract`

`Red`-`0` `Green`-`0` `Blue`-`0` `Bit Plane Order`-`BGR`

So the flag is `flag{remember_kids_protect_your_headers_7125}`.