import unittest

# PyCharm seems to think that these modules don't exist,
# even though these imports are performed correctly
# TODO Remove noinspection suppressions once this PyCharm bug is fixed

# noinspection PyUnresolvedReferences
from google_logo_present_test import GoogleLogoPresentTest
# noinspection PyUnresolvedReferences
from search_box_present_test import SearchBoxPresentTest
# noinspection PyUnresolvedReferences
from search_box_type_test import SearchBoxTypeTest
# noinspection PyUnresolvedReferences
from search_perform_test import SearchPerformTest
# noinspection PyUnresolvedReferences
from search_no_input_test import SearchNoInputTest

# The test cases are all in separate files, one method per class, one class per file. This is to prevent the possibility
# of tests leaking their state into other tests, and also to keep all tests succinct and easily extendable, movable, and
# replaceable.

smoke_tests = unittest.TestSuite([
    unittest.defaultTestLoader.loadTestsFromTestCase(GoogleLogoPresentTest),
    unittest.defaultTestLoader.loadTestsFromTestCase(SearchBoxPresentTest),
    unittest.defaultTestLoader.loadTestsFromTestCase(SearchBoxTypeTest),
    unittest.defaultTestLoader.loadTestsFromTestCase(SearchPerformTest),
    unittest.defaultTestLoader.loadTestsFromTestCase(SearchNoInputTest)
])

unittest.TextTestRunner().run(smoke_tests)
