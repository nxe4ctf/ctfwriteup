# picoCTF 2017: Leaf_of_the_Tree

**Level:** 1 **Category:** MISC **Point:** 20 **Description:**

>We found this annoyingly named directory tree starting at /problems/f8fc794974ad619254d983bc423608c6. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!

**Hint:**

>Tab completion is a wonderful, wonderful thing

## Write-up

Tab really is a wonderful, wonderful thing.
```
nxe@shell-web:~$ cd /problems/f8fc794974ad619254d983bc423608c6
nxe@shell-web:/problems/f8fc794974ad619254d983bc423608c6$ ls
nxe@shell-web:/problems/f8fc794974ad619254d983bc423608c6$ cd trunk/
...
```
Follow the trunk. And the flag at:
```
/problems/f8fc794974ad619254d983bc423608c6/trunk/trunk47a0/trun
k599f/trunk4e66/trunke117/trunk64f5/trunk9721/trunk1e42$
```
Using `cat flag`, The flag is `a2916629ba334b79632b6af945131ea2`.