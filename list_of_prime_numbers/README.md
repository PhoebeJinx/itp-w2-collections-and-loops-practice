# [itp-w1] List of Prime Numbers

Write a program that returns a list of prime numbers that are less than the max_number argument.

This can be a very intimidating problem at first glance. Where do you begin?
The trick to solving problems like this is to break it down into smaller chunks.

We can divide this into two parts: finding out if a number is prime, and creating the list of prime numbers. To do this, we will create a helper function `is_prime` to do the first part. We'll then use it in the main function to achieve our goal. **Divide and conquer**.

Note: 1 is not prime!!!

This is how the output should look. Best of luck!



```python
>>> _is_prime(5)
True
>>> _is_prime(4)
False
>>> list_of_prime_numbers(10)
[2, 3, 5, 7]
>>> list_of_prime_numbers(19)
[2, 3, 5, 7, 11, 13, 17, 19]
```
