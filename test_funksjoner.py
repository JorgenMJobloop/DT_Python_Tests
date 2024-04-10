import unittest
import funksjoner
# test cases that check for variable sanity
class TestVariables(unittest.TestCase):
    def test_assigned_variables(self):
        test_x = funksjoner.x
        self.assertEqual(test_x, 5)

    def test_reassignment(self):
        test_x = funksjoner.x
        self.assertEqual(test_x, 10)

    def test_types(self):
        test_string_y = funksjoner.string_y
        self.assertEqual(test_string_y, str)
        test_pi = funksjoner.pi
        self.assertEqual(test_pi,float) and self.assertEqual(test_pi, 3.14)
# test cases for loops
class TestLoops(unittest.TestCase):
    def test_for_loop(self):
        expected_iteration = [0,1,2,3,4]
        actual_iteration = funksjoner.for_loop()
        self.assertEqual(actual_iteration, expected_iteration)

# test cases for functions
class TestFunctions(unittest.TestCase):
    def test_add(self):
        result = funksjoner.add(5,5)
        self.assertEqual(result, 10)

    def test_greeting_function(self):
        name = "John Doe"
        self.assertEqual(funksjoner.greeting_function(name))

if __name__ == "__main__":
    unittest.main()