# picoCTF 2017: A Thing Called the Stack

**Level:** 2 **Category:** REVERSE ENGINEERING **Point:** 60 

**Description:**

>A friend was stacking dinner plates, and handed you [this](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_2/REVERSE_ENGINEERING/A_Thing_Called_the_Stack/assembly.s), saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

**Hint:**

<blockquote>Where is the return address saved on the stack?</blockquote>
<blockquote>Which commands actually affect the stack?</blockquote>

## Write-up

With each `pushl` the stack reducing ESP by 4. And the The last four instructions don't move the stack pointer.

``` 
foo:
    pushl %ebp -4
    mov %esp, %ebp
    pushl %edi    -4-4
    pushl %esi    -4-4-4
    pushl %ebx    -4-4-4-4
    sub $0xf8, %esp   -4-4-4-4-f8 = 0x108
    movl $0x1, (%esp)
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)
```

So the flag is `0x108`.
