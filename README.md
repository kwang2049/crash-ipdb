# crash-ipdb
Debug Python crashes conveniently: Whenever a Python code crashes, the [ipdb](https://github.com/gotcha/ipdb) (IPython debugger) debugger will be triggered. And the [pdb](https://docs.python.org/3/library/pdb.html) commands can be used to debug your crash.

## Usage
First install it with:
```bash
pip install crash-ipdb
```
Then import `crash_ipdb` in your Python and run your code as usual ([./example.py](example.py)):
```python
import crash_ipdb  # just import crash_ipdb in your Python code

## simple example of source code to be debugged ##
x = 1
y = 0

print(x/y)  # When you see '----> 7 print(x/y)', this will mean you have entered the ipdb, stopping at this line
```
You will find you have entered into ipdb and can use the [pdb commands](https://docs.python.org/3/library/pdb.html) to debug your code:
```bash
Traceback (most recent call last):
  File "example.py", line 7, in <module>
    print(x/y)  # When you see '----> 7 print(x/y)', this will mean you have entered the ipdb, stopping at this line
ZeroDivisionError: division by zero

> /home/ukp/kwang/crash-ipdb/crash-ipdb/example.py(7)<module>()
      3 ## simple example of source code to be debugged ##
      4 x = 1
      5 y = 0
      6 
----> 7 print(x/y)  # When you see '----> 7 print(x/y)', this will mean you have entered the ipdb, stopping at this line
```

## Reference
[xcodebuild/crash_on_ipy.py](https://gist.github.com/xcodebuild/3fef2c1e6eb109a91977)
