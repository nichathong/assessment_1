import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

findID = Solution.findID

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(findID(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([[1, 2, 3, 4, 5],3], 2)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([[2, 4, 6, 8, 10],7], -1)
        

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()