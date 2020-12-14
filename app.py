from flask import Flask,render_template,request,session,logging,url_for,redirect,jsonify
from flaskext.mysql import MySQL


app=Flask(__name__)


if __name__=="__main__":
	app.run(debug=True)

