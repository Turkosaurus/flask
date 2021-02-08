# Flask Tutorial
Corey Schafer YouTube series
[link to 1^st video](https://www.youtube.com/watch?v=MwZwr5Tvyxo)

---

## 1 - Getting Started

#### Install flask locally
3:30 `pip intstall flask` // install flask locally
> Check install
> - go to python interpreter
> - import flask (if no errors, then success)


#### Start Project
- open project directory
- create application.py
- paste following to begin
```from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"```

@decorators
: "a way to add additional functionality to additional functions" 