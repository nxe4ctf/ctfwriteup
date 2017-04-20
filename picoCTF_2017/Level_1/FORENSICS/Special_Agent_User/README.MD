# picoCTF 2017: Special Agent User

**Level:** 1 **Category:** FORENSICS **Point:** 50 **Description:**

>We can get into the Administrator's computer with a browser exploit. But first, we need to figure out what browser they're using. Perhaps this information is located in a network packet capture we took: [data.pcap](https://github.com/nxe4ctf/ctfwriteup/raw/master/picoCTF_2017/Level_1/FORENSICS/Special_Agent_User/data.pcap). Enter the browser and version as "BrowserName BrowserVersion". NOTE: We're just looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0).

**Hint:**

>Where can we find information on the browser in networking data? Maybe try [reading up on user-agent strings](www.useragentstring.com).

## Write-up

Tool:Wireshark.

Open the data.pcap with Wireshark.Then find the packet #93 and follow TCP stream of it:
```
GET / HTTP/1.1
User-Agent: Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))
Accept: */*
Host: 10.0.0.1
Connection: Keep-Alive
```
Copy the user-agent to the [given website](www.useragentstring.com) to analyze. The browsername and the browserversion is `IE 9.0`.
Therefore, The flag is `ie 9.0`.