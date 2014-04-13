flask-error
===========

Automatic error handler blueprints for Flask

How to Use it
-------------

First, Write Flask app as usual like this:

```python
from flask import Flask

# NOTE: Don't forget this line:
from flask.ext.error import errorhandler

app=Flask(__name__)

if __name__ == "__main__":
    app.run()
```

Next, insert "register_blueprint" like this:

```python
from flask import Flask

# NOTE: Don't forget this line:
from flask.ext.error import errorhandler

app=Flask(__name__)
app.register_blueprint(errorhandler)

if __name__ == "__main__":
    app.run()
```

Finally, let's raise the error!

```python
from flask import Flask

# NOTE: Don't forget this line:
from flask.ext.error import errorhandler

app=Flask(__name__)
app.register_blueprint(errorhandler)

@app.route("/test")
def not_implemented():
    raise NotImplementedError()

if __name__ == "__main__":
    app.run()
```
