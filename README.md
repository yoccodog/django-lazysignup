Introduction
============

``django-lazysignup`` is a package designed to allow users to interact with a
site as if they were authenticated users, but without signing up. At any time,
they can convert their temporary user account to a real user account.

http://django-lazysignup.readthedocs.org/

```
requirements
---
django-3.x
python-3.7.x
```

### What is this branch?

This is a branch that adds middleware that wraps every request to allow lazy users. It also makes the user superusers. So, it's dangerous.
