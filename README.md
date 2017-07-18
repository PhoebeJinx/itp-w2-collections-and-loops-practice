# Collections and loops practice

This project consists of small assignment functions to work in groups and practice collections and loops.  Please refer to each assignment directory for details.

## How to run tests

**Run tests for just one assignment**

```bash
$ py.test -v --tb=short create_box
```

![image](https://user-images.githubusercontent.com/872296/28190829-e38ca940-67fa-11e7-8e3a-d363ac5aecd8.png)

**Run tests matching a given name**

```bash
$ py.test -v --tb=short list_of_prime_numbers/ -k test_big_number_prime_false
```

![image](https://user-images.githubusercontent.com/872296/28190860-0ec010ca-67fb-11e7-893a-8765295826b9.png)

**Testing Python versions with TOX**

```bash
$ tox -epy27
```

![image](https://user-images.githubusercontent.com/872296/28190983-c13b11f0-67fb-11e7-93d2-c93f9f601072.png)
