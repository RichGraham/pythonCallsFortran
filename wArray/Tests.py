#!/usr/bin/env python
#*********WARNING:********* Do not edit this directly, instead copy the file elsewhere and edit or find and edit the ipython file/Users/pmzrsg/source/pythonCallsFortran/basic/ Tests.ipynb
#!/usr/bin/env python
# coding: utf-8
 
import unittest
import importlib
import callFortran
#importlib.reload(callFortran) #ipython_only
 
#importlib.reload(callFortran) #ipython_only
class TestFunctionCalls(unittest.TestCase):
    def testValues(self):
        self.assertAlmostEqual( callFortran.callFunction(0),2.0)
        self.assertAlmostEqual( callFortran.callFunction(2.5),4.5)
    
        
#unittest.main(argv=['first-arg-is-ignored'], exit=False) #ipython_only
 
 
class TestBlank(unittest.TestCase):
    
    def testBlank(self):
        pass
        
#unittest.main(argv=['first-arg-is-ignored'], exit=False) #ipython_only
 
 
unittest.main(argv=['first-arg-is-ignored'], exit=False)
 
 
 
