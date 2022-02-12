import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())