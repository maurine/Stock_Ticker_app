from flask import Flask, render_template, request, redirect
import sys
import quandl
import pandas
import re
import os
import plotticker as plotbt

#print('app.py is working')

app = Flask(__name__)

app.vars={}

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/userinput',methods=['GET','POST'])
def userinput():

  if request.method == 'GET':
    #print('In GET', file=sys.stderr)
    return render_template('userinput.html')
  #if request.method == 'POST':
  elif request.method == 'POST':
    #print('In POST', file=sys.stderr)
    #input data
    app.vars['name'] = request.form['ticket_input']
    app.vars['date'] = request.form['date_input']   
    
    #request data Note: empty for dates after 2018-03-27
    quandl.ApiConfig.api_key = 'u6K5RGjNFVTgN6xeSUSx'
    data=quandl.get_table('WIKI/PRICES', ticker='%s'%(app.vars['name']), date='%s-1,%s-2,%s-3,%s-4,%s-5,%s-6,%s-7,%s-8,%s-9,%s-10,%s-11,%s-12,%s-13,%s-14,%s-15,%s-16,%s-17,%s-18,%s-19,%s-20,%s-21,%s-22,%s-23,%s-24,%s-25,%s-26,%s-27,%s-28,%s-29,%s-30,%s-31'%(app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date'],app.vars['date']))
    #print('Collected data for the month', file=sys.stderr)
    #print(data, file=sys.stderr)
	
    #keep only close price data
    df_all=pandas.DataFrame(data,columns=['ticker','date','open','high','low','close','vol','exd','spl','adjopen','adjhigh','adjlow','adjclose','adjvol'])
	
    #create unique lines.html file
    filename='lines_%s_%s.html'%(app.vars['name'],app.vars['date'])
    outputfilepath=os.path.join('templates',filename)
    #print(outputfilepath, file=sys.stderr)
    #print(os.path.isfile(outputfilepath), file=sys.stderr)
    
    #plotting data for the month
    #print(df_all['date'], file=sys.stderr)
    x=[x.day for x in df_all['date'].tolist()]
    y=df_all['close'].values.tolist()
    plotbt.bt(x,y,app.vars['name'],app.vars['date'],outputfilepath)
    
    #output data
    return render_template(filename, d1=app.vars['name'],d2=app.vars['date'])
  else:
    print('Method is not a GET or POST', file=sys.stderr)
    
@app.route('/button/')
def button_clicked():
  print('Hello world!', file=sys.stderr)
  return redirect('/')  
  
if __name__ == '__main__':
  app.run(port=33507)