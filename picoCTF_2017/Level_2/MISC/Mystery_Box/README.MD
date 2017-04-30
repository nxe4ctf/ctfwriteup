# picoCTF 2017: Mystery Box

**Level:** 2 **Category:** MISC **Point:** 60 

**Description:**

>You've found a mystery machine with a sticky [note](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_2/MISC/Mystery_Box/note.txt) attached to it! Oh, there's also this [picture](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_2/MISC/Mystery_Box/MysteryBox.png) of the machine you found.

**Hint:**

<blockquote>It really gets your gears Turing.</blockquote>
<blockquote>I hear there's something Naval about it.</blockquote>

## Write-up

By googling the words in the note.txt, this challange seems like an Enigma Machine cryptography. Then I found a [website](http://enigma.louisedade.co.uk) could emulate the Enigma Machine.

``` 
Enigma Type: M3 (Navy/Army/Airforce)
Umkehrwalze: --- B ---
Walzenlage: I II III
Ringstellung: L O G
Grundstellung: P P P

Steckerbrett
G-L H-F
```

[Saved Settings Website](http://enigma.louisedade.co.uk/enigma.html?m3;b;b123;ALOG;APPP;FH-GL)

Then type the Geheimnis words in the note.txt. 

```
QUIT EPUZ ZLIN GIND EED
```

So the flag is `QUITEPUZZLINGINDEED`.