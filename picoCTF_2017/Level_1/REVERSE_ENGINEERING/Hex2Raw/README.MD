# picoCTF 2017: Hex2Raw

**Level:** 1 **Category:** REVERSE ENGINEERING **Point:** 20 **Description:**

>This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/88518d23aee7ee21e50bdd8414a404c1 and turn that Hex2Raw!

**Hint:**

>Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.

## Write-up

Firstly, install the pycrypto lib:

``` 
$ cd /problems/88518d23aee7ee21e50bdd8414a404c1
$ ls
flag hex2raw input
$ ./hex2raw
Give me this in raw form (0x41 -> 'A'):                                      
7ca67167db329a5d1508cc4ad5380678

You gave me:
^C
$ echo 7ca67167db329a5d1508cc4ad5380678 | xxd -r -p | ./hex2raw
Give me this in raw form (0x41 -> 'A'):                                      
7ca67167db329a5d1508cc4ad5380678                                             
                                                                             
You gave me:                                                                 
7ca67167db329a5d1508cc4ad5380678                                             
Yay! That's what I wanted! Here be the flag:                                 
75d3080d00407fa709c18a6cc69d1edc
```

So the flag is `75d3080d00407fa709c18a6cc69d1edc`.
