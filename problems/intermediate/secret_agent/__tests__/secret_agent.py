import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from secret_agent import crackCodeN

def test():
    if crackCodeN("0") != ['0', '8']:
        print("❌ failed python test 1")
    if crackCodeN("2") != ['1', '2', '3', '5']:
        print("❌ failed python test 1")
    else:
        print("✅ passed all python tests")


if __name__ == "__main__":
    test()