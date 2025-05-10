
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Grid_Cleaner import gridCleaner

def test():
    if gridCleaner([[1]],0,0,1,0) != [[0,0]]:
        
        print("❌ python test failed")
    else: print("✅ python test passed")  

if __name__ == "__main__":
    test()