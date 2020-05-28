#!/usr/bin/python

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
#from weather import query_api
from quote import query_stock

webapp = Flask(__name__) #create a flask webapp

@webapp.route("/") #"GET / HTTP/1.1"
def index():
    return render_template(
        'weather.html',
        data=[{'name':'AMD'}, {'name':'BA'}, {'name':'CVX'},
        {'name':'DIS'}, {'name':'EBAY'}, {'name':'FB'},
        {'name':'GILD'}, {'name':'HD'}, {'name':'INTC'},
        {'name':'JPM'}])

@webapp.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_stock(select)
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