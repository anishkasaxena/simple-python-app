import unittest
from app import hello_world()  # Assuming hello_world_function is defined in hello_world.py

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        # Call the hello_world_function
        result = hello_world()
        
        # Assert that the result is as expected
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()

