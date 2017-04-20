# picoCTF 2017: Leaf_of_the_Tree

**Level:** 1 **Category:** MISC **Point:** 20 **Description:**

>I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:44909?

**Hint:**

<blockquote>Use the nc command to connect!</blockquote>

<blockquote>I hear python is a good means (among many) to generate the needed input.</blockquote>>

<blockquote>It might help to have multiple windows open</blockquote>

## Write-up

After connecting the server, it will ask you to input a alphabet for many times and a number behind them. The first time I used Python to print the neededword and copy to the shell:
```
print "x" * times
```
It is a noob way, then I found a Python [script](https://github.com/nxe4ctf/ctfwriteup/blob/master/picoCTF_2017/Level_1/MISC/looooong/script.py) to do this(Thanks to [LFlare](https://github.com/LFlare)).

The flag is `with_some_recognition_and_training_delusions_become_glimpses_84bb3b369444af45f140fa500f5e54c3`.