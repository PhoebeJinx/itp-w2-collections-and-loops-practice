# [itp-w1] Create Box

Write a program that takes three inputs: height, width, and character.
Use your knowledge of loops to create a box made of characters based on the inputs.

Note: You need to `return` your box, not just print it.

```python
>>> create_box(3, 4, '*')
'****
 ****
 ****'
>>> create_box(2, 2, '@')
'@@
 @@'
```

**Ideas for enhancements in case of extra time:**
- Add error checking to make sure the width and height is greater or equal to 1
- Add an extra unit test for the third case in the tests file
- For an extra challenge, make it so only the outer border of the box shows and it is not filled in.
  Make this a separate function and add unit tests for it.
