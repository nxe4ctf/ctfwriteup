# picoCTF 2017: Digital Camouflage

**Level:** 1 **Category:** FORENSICS **Point:** 50 **Description:**

>We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: [data.pcap](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_1/FORENSICS/Digital_Camouflage/data.pcap).

**Hint:**

<blockquote>It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?</blockquote>
<blockquote>If you think you found the flag, but it doesn't work, consider that the data may be encrypted. </blockquote> 

## Write-up

Tool:Wireshark.

Open the data.pcap with Wireshark.Then find the packet #122(main.html)
```
HTML Form URL Encoded: application/x-www-form-urlencoded
    > Form item: "userid" = "randled"
    > Form item: "pswrd" = "OFBGRW8wdHRIUQ=="
```
It seems like a base64 encode string. So using the base64 decode online tools to decode it. 
The flag is `8PFEo0ttHQ`.