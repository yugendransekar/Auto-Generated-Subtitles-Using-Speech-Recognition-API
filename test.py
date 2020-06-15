import time 
import progressbar 
  
widgets = [' [', 
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'), 
         '] ', 
           progressbar.Bar('*'),' (', 
           progressbar.ETA(), ') ', 
          ] 
  
bar = progressbar.ProgressBar(max_value=200,  
                              widgets=widgets).start() 
  
for i in range(200): 
    time.sleep(0.1) 
    bar.update()
    i=i+1 