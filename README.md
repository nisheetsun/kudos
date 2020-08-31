# kudos

## How to run
* install packages from requirements.txt
* run ```./manage.py runserver 0.0.0.0:8000```
* open ```http://127.0.0.1:8000/blog/```

## Behaviours

### When not Authorised
* can see list of blogs already published
* can give kudos to blogs
* can see list of authors
* can see author details and blogs by author

### When Authorised as a user
* all the above plus mentioned below
* can create a blog
* can update the blog belonging to user
* can unpublish the blog belonging to user
* can make a blog private
* can access draft page to see drfat blogs


### When Authorised as a staff
* all the above plus mentioned below
* can visit waiting tab and publish a blog.
* can un-publish any blog

### Superuser
* all and everything. You are the God.
