import crash_ipdb  # just import crash_ipdb in your entry-point Python code

## below is a simple example of when the Python crashes due to some bugs ##
x = 1
y = 0

print(x/y)  # When you see '----> 7 print(x/y)', this will mean you have entered the ipdb, stopping at this line