from distutils.core import setup

# This file is for setting up and installing the framework tfhw_main which the Selenium tests in this project use.
#
# This is not the PyWebDriverFramework, this framework is specific to this project. It should be used to store all
# non-test code that the tests use while running, such as page objects, custom expected conditions, custom exceptions,
# external service connection managers, and other utilities.

setup(name='tfhw_main',
      version='0.0.1',
      description='True Fit Take Home Test Framework',
      packages=['tfhw_main', 'tfhw_main.common.loadables.pageobjects'])
