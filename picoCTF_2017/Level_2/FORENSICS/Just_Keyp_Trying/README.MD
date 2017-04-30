# picoCTF 2017: Just Keyp Trying

**Level:** 2 **Category:** FORENSICS **Point:** 70 

**Description:**

>Here's an interesting capture of some data. But what exactly is this data? Take a look: [data.pcap](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_2/FORENSICS/Just_Keyp_Trying/data.pcap)

**Hint:**

<blockquote>Find out what kind of packets these are. What does the info column say in Wireshark/Cloudshark?</blockquote>
<blockquote>What changes between packets? What does that data look like?</blockquote>
<blockquote>Maybe take a look at http://www.usb.org/developers/hidpage/Hut1_12v2.pdf?</blockquote>

## Write-up

Open the .pcap file with Wireshark. All packages are USB packages, and the deferences of them are `Leftover Captured Data`. Consulting the [USB HID Usage Tables](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf) that given at the hint, we know that the captured data is USB keyboard code.(In the 53 page). Now we use the tshark(in the wireshark folder) to extract all the `Leftover Captured Data`. 

``` 
tshark.exe -r data.pcap -T fields -e usb .capdata > usbdata.txt
```

Then open the [usbdata.txt](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_2/FORENSICS/Just_Keyp_Trying/usbdata.txt) with Notepad++:

```
00:00:09:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0f:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:04:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0a:00:00:00:00:00
00:00:00:00:00:00:00:00
20:00:00:00:00:00:00:00
20:00:2f:00:00:00:00:00
20:00:00:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:13:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:15:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:20:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:22:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:22:00:00:00:00:00
00:00:00:00:00:00:00:00
20:00:00:00:00:00:00:00
20:00:2d:00:00:00:00:00
20:00:00:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:27:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:11:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:1a:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:04:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:15:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:07:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:16:00:00:00:00:00
00:00:00:00:00:00:00:00
20:00:00:00:00:00:00:00
20:00:2d:00:00:00:00:00
20:00:00:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:20:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:04:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:1e:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:27:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:1e:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:20:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:21:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:08:00:00:00:00:00
00:00:00:00:00:00:00:00
20:00:00:00:00:00:00:00
20:00:30:00:00:00:00:00
20:00:00:00:00:00:00:00
00:00:00:00:00:00:00:00
01:00:00:00:00:00:00:00
01:00:06:00:00:00:00:00
```

We could see the number in the third column is the keypress code. Using the Python [script](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_2/FORENSICS/Just_Keyp_Trying/decode.py) to decode it.

The flag is `FLAG{PR355_0NWARDS_3A10134E}`.