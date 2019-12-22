# jsdocify

If you have comments that look like this:

```javascript
function superFunction()
// this is a super fantastic comment!
// it is ripe with information on this
// function's many assumptions, and also
// devoid of superfluous information.
{
  return bestFunction() && {} || !0;

  function bestFunction()
  // this comment is also useful.
  // however many linters hate this comment.
  // all comments are born equal and are
  // entitled to certain inalienable rights.
  // however linters do not support comment
  // equality. and for this reason we must
  // run jsdocify to save this comment 
  // and de-anger our linter.
  {
    return ""
  }
}
```

Then you run `python3 jsdocify --inplace FILE` and it becomes:

```javascript
/**
 * this is a super fantastic comment!
 * it is ripe with information on this
 * function's many assumptions, and also
 * devoid of superfluous information.
 */
function superFunction() {
  return bestFunction() && {} || !0;

  /**
   * this comment is also useful.
   * however many linters hate this comment.
   * all comments are born equal and are
   * entitled to certain inalienable rights.
   * however linters do not support comment
   * equality. and for this reason we must
   * run jsdocify to save this comment
   * and de-anger our linter.
   */
  function bestFunction() {
    return ""
  }
}
```


How beautiful!
