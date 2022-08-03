#!/usr/bin/env python
#*********WARNING:********* Do not edit this directly, instead copy the file elsewhere and edit or find and edit the ipython file/Users/pmzrsg/source/pythonCallsFortran/wArray/ Tests.ipynb
#!/usr/bin/env python
# coding: utf-8
 
import unittest
import importlib
import numpy as np
import callFortran
#importlib.reload(callFortran) #ipython_only
 
#importlib.reload(callFortran) #ipython_only
class TestFunctionCalls(unittest.TestCase):
    def testValues(self):
        checkArray( 10,3)
        checkArray( 1,35)
        checkArray( 2,4)
        checkArray( 8,1)
        checkArray( 11,6)
        checkArray( 100,3000)
        
        
#unittest.main(argv=['first-arg-is-ignored'], exit=False) #ipython_only
 
def checkArray( rows, columns):
    u = np.linspace(0, 1.0, num=rows*columns)
    x = np.reshape(u, (rows, columns))
    
    actual= callFortran.callFunction( x)
    expected = np.exp(x)
    np.testing.assert_almost_equal(actual,expected)
    
 
class TestBlank(unittest.TestCase):
    
    def testBlank(self):
        pass
        
#unittest.main(argv=['first-arg-is-ignored'], exit=False) #ipython_only
 
 
unittest.main(argv=['first-arg-is-ignored'], exit=False)
 
 
 
