# picoCTF 2017: keyz

**Level:** 1 **Category:** CRYPTOGRAPHY **Point:** 20 **Description:**

>While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com

**Hint:**

<blockquote>There are plenty of tutorials out there. This one covers key generation: https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html</blockquote>

<blockquote>Then, use the web shell to copy/paste it, and use the appropriate tool to ssh to the server using your key</blockquote>

## Write-up

First, use your own computer to generate a public key.

``` 
ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:HT0kn4JUZLcmfjRUmlTiC5iK79RT00gH4Dj/+392bUo root@kali
The key's randomart image is:
+---[RSA 2048]----+
|        o+* *oo  |
|       + = @ *   |
|      o = * #    |
|     . + + @ +   |
|    . . S * +    |
|     . . o o     |
|      o o .   E .|
|     o   . . .  *|
|      .   ....o=.|
+----[SHA256]-----+
```

Next, copy the public key(id_rsa.pub) in your computer to the web shell as the challenge said.

```
echo "{your public key}" >> ~/.ssh/authorized_keys
```

Then, use ssh tool with your own computer to connect to the server.

```
ssh nxe@shell2017.picoctf.com
Congratulations on setting up SSH key authentication!
Here is your flag: who_needs_pwords_anyways

```

So the flag is `who_needs_pwords_anyways`.