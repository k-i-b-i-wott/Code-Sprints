import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from organizing_container import organizingContainers

def test_organizing_containers():
    containers = [[1, 4], [2, 3]]
    result = organizingContainers(containers)
    assert result == "Impossible", f"Expected Impossible, got {result}"

    print("✅ Python test passed!")

if __name__ == "__main__":
    test_organizing_containers()
