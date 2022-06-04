By using this script you can combine several pulses into one rhythmic line (-> union of residual classes). 

After running the main.py with Python3, Terminal prompts you for values. 
And writes resulting .xml file into the same directory where main.py resides. 

The length (-> period) of the resulting rhythm is the lowest common denominator of pulses (utilizes math.lcd , therefore Python 3.9> is necessary). 
This program depends on scamp library; please install it beforehand.
> pip3 install scamp

