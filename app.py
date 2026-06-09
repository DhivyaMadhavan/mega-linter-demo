# app.py (test version)

import json
import os   # unused import → should trigger lint warning

def bad_function():
print("This line has bad indentation")   # indentation error

def unused_function(x, y):
    return x + y   # unused function → should trigger lint warning
