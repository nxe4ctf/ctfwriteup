# picoCTF 2017: Leaf_of_the_Forest

**Level:** 1 **Category:** MISC **Point:** 30 **Description:**

>We found an even bigger directory tree hiding a flag starting at /problems/b88cc963bcaf6042d143bfef6db2100b. It would be impossible to find the file named flag manually...

**Hint:**

>Is there a search function in Linux? Like if I wanted to 'find' something...

## Write-up

Using the `find` is easy to find the flag.

```
nxe@shell-web:/problems/b88cc963bcaf6042d143bfef6db2100b$ find -name flag -exec cat {} \;
```

The flag is `eb34ff576412f11b06fb68884bef0ec5`.