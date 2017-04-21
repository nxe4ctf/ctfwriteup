# picoCTF 2017: computeRSA

**Level:** 1 **Category:** CRYPTOGRAPHY **Point:** 50 **Description:**

>RSA encryption/decryption is based on a formula that anyone can find and use, as long as they know the values to plug in. Given the encrypted number 150815, d = 1941, and N = 435979, what is the decrypted number?

**Hint:**

>decrypted = (encrypted) ^ d mod N

## Write-up

Using Python:

```
>>> encrypted = 150815
>>> d = 1941
>>> N = 435979
>>> decrypted = ((encrypted) ** d ) % N
>>> print(decrypted)
133337

```

So the flag is `133337`.
