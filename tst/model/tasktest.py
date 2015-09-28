import unittest, sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../src/model'))
from task import Task

class TaskTest(unittest.TestCase):

    def testGet(self):
        testTask = Task("this is the description", 1)
        self.assertEqual(testTask.getDescription(), "this is the description")
        self.assertEqual(testTask.getRepititions(), 1)

    def testFormat(self):
        testTask = Task("this is the {} description", 2)
        self.assertEqual(testTask.toDescription(), "this is the 2 description")

if __name__ == '__main__':
    unittest.main()
