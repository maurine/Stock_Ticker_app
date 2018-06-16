from bokeh.plotting import figure, output_file, show, save
import os

def bt(x,y,t,m,outputfilepath):
  #print('Hello World')
  
  if os.path.isfile(outputfilepath):
    os.unlink(outputfilepath)

  # create a new plot with a title and axis labels
  p = figure(title="Closing Price for Ticker %s in the Month of %s"%(t,m), x_axis_label='Day', y_axis_label='Closing Price')
  
  # add a line renderer with legend and line thickness
  p.line(x, y, legend="Closing Price", line_width=2)

  save(p,outputfilepath)