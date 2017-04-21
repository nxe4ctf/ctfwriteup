# picoCTF 2017: Lazy Dev

**Level:** 1 **Category:** CRYPTOGRAPHY **Point:** 50 **Description:**

>I really need to login to this [website](http://shell2017.picoctf.com:35895), but the developer hasn't implemented login yet. Can you help?

**Hint:**

<blockquote>Where does the password check actually occur?</blockquote>
<blockquote>Can you interact with the javascript directly?</blockquote>

## Write-up

Viewing the JS source file with F12, the first several lines are:

``` 
function validate(pword){
  //TODO: Implement me
  return false;
}
```

So we just need let it return true, type these in the console of the Browser DevTools:

```
function validate(pword){
  //TODO: Implement me
  return true;
}
```

Then click `Submit`.

So the flag is `client_side_is_the_dark_sidebde1f567656f8c9b654a1ec24e1ff889`.


