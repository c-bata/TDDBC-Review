# -*- coding: utf-8 -*-
__author__ = 'masashi'

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../app")
from task import Task


class TaskTests(unittest.TestCase):
    def test_create_task(self):
        task = Task()
        self.assertIsInstance(task, Task)


if __name__ == '__main__':
    unittest.main()
