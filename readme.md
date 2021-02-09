# Flask Tutorial
Corey Schafer - YouTube Flask series [(link to first video)](https://www.youtube.com/watch?v=MwZwr5Tvyxo)

---

## 1 - Getting Started

#### Install flask locally
`pip intstall flask` // install flask locally
> Check install
> - go to python interpreter
> - import flask (if no errors, then success)


#### Start Project
- open project directory
- create application.py [^1] with the following code
```
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!" 
```

@ decorators
: "a way to add additional functionality to functions"

#### Set environment variables
- Linux `export FLASK_APP=application.py`
- Windows `set FLASK_APP=application.py`

#### Test flask server
- `flask run`
- take note of IP address:port, (localhost):5000
- note that `ctrl-C` restart required after changes are saved

#### Enable debug mode
- Linux `export FLASK_DEBUG=1`
- Windows `set FLASK_DEBUG=1`
This enables automatic change updates on reload

#### Run directly using python (optional)
Add to `application.py`:
```
if __name__ = '__main__':
    app.run(debug=True)
```

Now, instead of using `flask run` and using environment variables, run server by invoking `python application.py`

#### Add more routes
- add `/home` to `/`
- rename `hello()` to `home()`
```
@app.route("/")
@app.route("/home")
def home():
    return "Hello World!" 

@app.route("/about:)
def about ():
    return "<h1>About</h1>
```

###### Footnotes
[^1]: Though Corey uses `flaskblog.py`, I have opted for the standard use of `application.py`

- - -

## 2 - Templates & Variables

#### Create Templates Directory
`mkdir templates`
`cd templates`
`touch home.html`

#### Import "render_template"
`from flask import Flask, render_template`
change `return` to `render_template('home.html')`

#### Create Global Dictionaries for Post Data
posts = {}

TODO


#### Pass Variables
`render_template('home.html' posts=posts)`

#### Loop Jinja Templates
```
    <body>
        {% for post in posts %}
            <h1>{{ post.title }}</h1>
            <p>By {{ post.author }} on {{ post.date_posted }} </p>
            <p>{{ post.content</p> 
        {% endfor %}
    </body>
```

#### Create Conditional Title
```
    <head>
        {% if title %}
            <title>Flask Blog - {{ title }}</title>
        {% else %}
            <title>Flask Blog</title>
        {% endif %}
    </head>
```

#### About Page: hard code title variable
`return render_template('about.html', title='About')`


#### Template Inheritance
- create layout.html, use block keyword `{% block content %}{% endblock %}`

- change home.html to extend layout.html
```
{% extends "layout.html" %}
{% block content %}
    {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>By {{ post.author }} on {{ post.date_posted }} </p>
        <p>{{ post.content</p> 
    {% endfor %}
{% endblock content %}
```
