#!/usr/bin/python

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
#from weather import query_api
from quote import query_stock

webapp = Flask(__name__) #create a flask webapp

@webapp.route("/") #"GET / HTTP/1.1"
def index():
    data = []
    error = None
    symbol = 'AMD'
    resp = query_stock(symbol)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)


if __name__ == "__main__":
    webapp.run(host='0.0.0.0', debug=True)
