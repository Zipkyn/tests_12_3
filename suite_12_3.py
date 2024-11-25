import unittest
from tests_12_3 import RunnerTest
from tests_12_3 import TournamentTest

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    runner.run(suite)


