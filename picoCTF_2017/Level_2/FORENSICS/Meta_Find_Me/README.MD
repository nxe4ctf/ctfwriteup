# picoCTF 2017: Meta Find Me

**Level:** 2 **Category:** FORENSICS **Point:** 70 

**Description:**

>Find the location of the flag in the image: [image.jpg](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_2/FORENSICS/Meta_Find_Me/image.jpg). Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

**Hint:**

>How can images store location data? Perhaps search for GPS info on photos.

## Write-up

Firstly, right click the file to see the properties of the image. We could get the GPS information:

``` 
GPS
Latitude 7; 0; 0
Longitude 96; 0; 0
```

Then open the file with Notepad++, search the `flag`:

```
Your flag is flag_2_meta_4_me_<lat>_<lon>_1c1f. Now find the GPS coordinates of this image! (Degrees only please)"
```

So the flag is `flag_2_meta_4_me_7_96_1c1f`.