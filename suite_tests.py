import unittest
import HtmlTestRunner
from tests import test_disappearing_elements
from tests import test_dropdown
from tests import test_key_presses
from tests import test_login
class TestSuite(unittest.TestSuite):

    def test_suite(self):
        smoke_tests = unittest.TestSuite()
        smoke_tests.addTest([unittest.defaultTestLoader.loadTestsFromTestCase(test_disappearing_elements.Disappearing_elements),
                             unittest.defaultTestLoader.loadTestsFromTestCase(test_dropdown.Dropdown),
                             unittest.defaultTestLoader.loadTestsFromTestCase(test_key_presses.Key_presses),
                             unittest.defaultTestLoader.loadTestsFromTestCase(test_login.Login)])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports =True, report_name="suiteCodePen").run(smoke_tests)