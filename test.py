#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, url_for, Response
import json

from flask.ext.error import errorhandler, NotFound

app = Flask(__name__)
app.register_blueprint(errorhandler)


@app.route("/")
def hello():
    routes = list()
    for rule in app.url_map.iter_rules():
        routes.append({
            "methods": list(rule.methods),
            "url": str(rule)
            })
    # return jsonify(routes)
    response = Response(mimetype="application/json")
    response.data = json.dumps(routes, indent="  ")
    return response


@app.route("/value_err")
def value_err():
    raise ValueError("Value Error")


@app.route("/key_error")
def key_error():
    d = {
        "a": "test1",
        "b": "test2"
    }
    return d["c"]


@app.route("/attr_err")
def attr_err():
    class Empty(object):
        pass

    empty = Empty()
    return empty.test


@app.route("/type_err")
def type_err():
    return bin(3.14159265358979)


@app.route("/not_implemented")
def not_implemented():
    raise NotImplementedError()


@app.route("/notfound")
def not_found():
    raise NotFound()


@app.route("/notfound/additional")
def not_found_additional():
    additonal = {
        "Additional Info": {
            "Code": 404,
            "Message": "This is an additional message"
        }
    }
    raise NotFound("Not Found with additional information", **additonal)

if __name__ == "__main__":
    app.run(debug=True)
