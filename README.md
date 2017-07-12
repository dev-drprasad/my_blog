# My Personal Blog
Developed using Django

[live demo](http://blog.reddyprasad.me/posts)

## How to Install
First clone the repo using
`git clone https://github.com/dev-drprasad/my_blog.git`

Change to project directory using
`cd my_blog`

Install project requirements
`pip install -r requirements.txt`

Rename the file `.env.example`
`mv .env.example .env`

Run the migrations
`cd src`
`python manage.py migrate`

Run the development web server
`python manage.py runserver`

Thats it! Open browser with url http://localhost:8000

