import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from password_Leak import passwordLeaked

def password_leakTest():
    if passwordLeaked("cbaebabacd", "abc") != [0,6]:
        print("❌ failed python test")
    else:
        print("✅ passed python tests")


if __name__ == "__main__":
    password_leakTest()