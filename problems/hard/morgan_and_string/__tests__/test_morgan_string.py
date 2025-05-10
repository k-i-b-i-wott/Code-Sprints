import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from morgan_string import morganAndString

def test_case_1():
    assert morganAndString("ACA", "BCF") == "ABCACF"

def test_case_2():
    assert morganAndString("JACK", "DANIEL") == "DAJACKNIEL"
    

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    print("All tests passed!")
    # Add more test cases as needed    
