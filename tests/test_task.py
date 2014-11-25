# -*- coding: utf-8 -*-
__author__ = 'masashi'

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../app")
from task import Task


class TaskTests(unittest.TestCase):
    def create_task(self, summary):
        return Task(summary)

    def test_create_task_with_summary1(self):
        summary = 'summary1'
        task = self.create_task(summary)
        self.assertEqual(task.summary, summary)

    def test_create_task_with_summary2(self):
        summary = 'summary2'
        task = self.create_task(summary)
        self.assertEqual(task.summary, summary)


if __name__ == '__main__':
    unittest.main()