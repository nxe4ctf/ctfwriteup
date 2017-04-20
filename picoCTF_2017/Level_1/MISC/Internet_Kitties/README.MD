# picoCTF 2017: Internet Kitties

**Level:** 1 **Category:** MISC **Point:** 10 **Description:**

>I was told there was something at IP shell2017.picoctf.com with port 28669. How do I get there? Do I need a ship for the port?

**Hint:**

<blockquote>Look at using the netcat (nc) command!</blockquote>
<blockquote>To figure out how to use it, you can run "man nc" or "nc -h" on the shell, or search for it on the interwebz</blockquote> 

## Write-up

Using the nc command to get flag.
```
nxe@shell-web:~$ nc shell2017.picoctf.com 28669
Yay! You made it!                                                            
Take a flag!                                                                 
648defaaba45452729b7179f0603df05
```

The flag is `648defaaba45452729b7179f0603df05`.