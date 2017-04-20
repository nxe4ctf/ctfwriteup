# picoCTF 2017: Substitute

**Level:** 1 **Category:** CRYPTOGRAPHY **Point:** 40 **Description:**

>A wizard (he seemed kinda odd...) handed me [this](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_1/CRYPTOGRAPHY/Substitute/cipher.txt). Can you figure out what it says?

**Hint:**

>There are tools that make this easy this.

## Write-up

At first, I thought the way of encryption was Caesar Cipher. But it wasn't.
Then I began to analyze the cipher string. The first word is `MIT`. And it appears at the begin of a sentence many times. So it may be `the`. Next, I found two 8-character month name that was encrypted and the last five characters are `TDZTK`, that were encypted `EMBER`... The complete process is shown below:

``` 
1.MIT:
  THE
    M-T
    I-H
    T-E
2.RTETDZTK
  DECEMBER
    R-D
    E-C
    D-M
    Z-B
    K-R
3.FGXTDZTK
  NOVEMBER
    F-N
    G-O
    X-V
4.UTFTKAMTR
  GENERATED
    U-G
    A-A
5.ZARUTL
  BADGES
    L-S
6.MTDHTKTR
  TEMPERED
    H-P
7.HKOFEOHAS
  PRINCIPAL
    H-P
    O-I
    S-L
8.DAKQGX
  MARKOV
    Q-K
9.YSAU
  FLAG
    Y-F
```

So the first three words are `THE FLAG IS`. Therefore, decode the fourth word:

```
OYGFSBDGRTKFEKBHMGCALSOQTMIOL
IFONLYMODERNCRYPTOWASLIKETHIS
```

The flag is `IFONLYMODERNCRYPTOWASLIKETHIS`.

PS:The fastest way is use the [tool](http://quipqiup.com/)(Thanks to [LFlare](https://github.com/LFlare)). Using that tool makes this challenge so easy...