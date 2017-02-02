# jsdocify

If you have comments that look like this:
```javascript


function superFunction()
// do a super fantastic thing
// but dont do it if I say not to
// because this function is hard
{
  return !0;

  function whatIsHoisting()
  // this function
  // returns
  // a string
  // explaining what
  // hoisting is
  // to people 
  // who write
  // comments
  // like
  // this
  {
    return "Hoisting is something that the person who writes comments like the ones preceeding this function body should have done above the function."
  }
}
```

```javascript
/**
* do a super fantastic thing
* but dont do it if I say not to
* because this function is hard
*/
function superFunction() {
  return !0;

 /**
  * this function
  * returns
  * a string
  * explaining what
  * hoisting is
  * to people 
  * who write
  * comments
  * like
  * this
  */
  function whatIsHoisting() {
    return "Hoisting is something that the person who writes comments like the ones preceeding this function body should have done above the function."
  }
}
```



  
