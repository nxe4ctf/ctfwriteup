# picoCTF 2017: computeAES

**Level:** 1 **Category:** CRYPTOGRAPHY **Point:** 50 **Description:**

>You found this [clue](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_1/CRYPTOGRAPHY/computeAES/clue.txt) laying around. Can you decrypt it?

**Hint:**

>Try online tools or python

## Write-up

Firstly, install the pycrypto lib:

``` 
// pip install pycrypto 
// An error will occurred: 'ImportError: No module named Crypto.Cipher'
easy_install pycrypto
```


```
py -2 decode.py
flag{do_not_let_machines_win_2d4975bc}__________
```

So the flag is `flag{do_not_let_machines_win_2d4975bc}`.
