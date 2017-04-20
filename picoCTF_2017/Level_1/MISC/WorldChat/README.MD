# picoCTF 2017: WorldChat

**Level:** 1 **Category:** MISC **Point:** 10 **Description:**

>We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:61161. Remember to use Ctrl-C to cut the connection if it overwhelms you!

**Hint:**

>There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)

## Write-up

First try:

```
ncat shell2017.picoctf.com 61161 | grep flag
```

Output:

```
12:52:53 ihazflag: Hungry jackolanterns want to see me to create a self driving car
12:52:53 noihazflag: Only us , in my well-educated opinion, are our best chance to drink your milkshake
12:52:53 noihazflag: I is our best chance to generate fusion power
12:52:54 personwithflag: Several heavily mustached dolphins are the best of friends for what, I do not know
12:52:55 personwithflag: Several heavily mustached dolphins , in my opinion, are our best chance to create a self driving car
12:52:56 ihazflag: Scary pandas have demanded my presence for what, I do not know
12:52:56 personwithflag: A huge moose wants to see me for the future of humanity
12:52:57 whatisflag: A small moose will never understand me to create a self driving car
12:52:57 noihazflag: Hungry jackolanterns give me hope to understand me
12:52:57 personwithflag: your dad is our best chance to create a self driving car
12:52:57 whatisflag: my homie wants to steal my sloth to drink your milkshake
12:52:58 personwithflag: A small moose totally understands me and my pet sloth to help me spell 'raspberry' correctly
12:52:58 noihazflag: my homie wants to steal my sloth to generate fusion power
12:52:58 flagperson: this is part 1/8 of the flag - 1a2e
12:52:59 personwithflag: Scary pandas want to see me to generate fusion power
12:52:59 flagperson: this is part 2/8 of the flag - 3d0a
```

Many usernames include `flag`, so I have to press Ctrl+C... But I have known the  structure of messages that include the flag.

Second try:
```
ncat shell2017.picoctf.com 61161 | grep -E "this is part"
```

Output:
```
12:54:59 flagperson: this is part 1/8 of the flag - 1a2e
12:55:00 flagperson: this is part 2/8 of the flag - 3d0a
12:55:00 flagperson: this is part 3/8 of the flag - 6310
12:55:02 flagperson: this is part 4/8 of the flag - 682c
12:55:03 flagperson: this is part 5/8 of the flag - 6be0
12:55:03 flagperson: this is part 6/8 of the flag - e319
12:55:07 flagperson: this is part 7/8 of the flag - d1b5
12:55:09 flagperson: this is part 8/8 of the flag - 2f53
```

The flag is `1a2e3d0a6310682c6be0e319d1b52f53`.