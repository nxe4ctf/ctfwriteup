# picoCTF 2017: Raw2Hex

**Level:** 1 **Category:** REVERSE ENGINEERING **Point:** 20 **Description:**

>This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/45f3b0abcf176b7cf7c1536b28d05d72 and turn that Raw2Hex!

**Hint:**

>Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.

## Write-up


``` 
$ cd /problems/88518d23aee7ee21e50bdd8414a404c1
$ ls
flag raw2hex
$ ./raw2hex
The flag is:v\h3-                                                            
                 
$ ./raw2hex | xxd -p
54686520666c61672069733acc76ae5c1b19d06897338d2deaa50bf0
```
The hex ascii value of `:` is `3a`

So the flag is `cc76ae5c1b19d06897338d2deaa50bf0`.
