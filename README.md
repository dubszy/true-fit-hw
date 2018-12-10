# True Fit Take Home Test
This is a set of
[Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/) tests
written in [Python](https://www.python.org/) using the
[Page Object Model](https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#page-object-design-pattern)
implemented with the [Python WebDriver wrapper framework](https://github.com/dubszy/PyWebDriverFramework)
I have also written.

## Project Structure
##### Google Home Page Test Plan.xlsx
Test Plan for the Google home page as an Excel spreadsheet
##### Google Home Page Test Plan.csv
A CSV version of the test plan
##### requirements.txt
Python package dependencies that this project uses
##### setup.sh
Script to setup the environment for this project
##### drivers/
Directory that the WebDriver binaries are placed in by the setup script
##### PyWebDriverFramework/
The PyWebDriverFramework Git submodule that this project uses
##### true_fit_hw/tests/
The Selenium tests
##### true_fit_hw/tfhw_main/
Framework for storing all non-test code that the tests use while running

## Prerequisites
This project requires the following:
- MacOS machine with curl, unzip, tar, Python 3.6+, pip3, and pytest 3 installed.
- Chrome version 69+ and Firefox version 57+

## Download
To download and start using this project you can do any of the following:
- Download a [release](https://github.com/dubszy/true-fit-hw/releases)
- Download a specific branch as a ZIP by selecting the branch to download from
the "Branch" dropdown menu, then using the "Clone or download" dropdown menu and
clicking "Download ZIP"
- Clone it in a CLI: `git clone git@github.com:dubszy/true-fit-hw.git`

## Setup
Once the project is downloaded, run the following command to set it up: `./setup.sh`, which will check for:
- curl
- unzip
- tar
- python3
- pip3

If there was an error locating any of these, the script will report as such. `curl`, `unzip`, and `tar` should already
be installed on your system, so if an error is reported for any of those, it may be indicative of an underlying issue.
If python3 is not found, [this guide](https://docs.python-guide.org/starting/install3/osx/) will help you install it
successfully.

After checking prerequisites, the setup script will fetch the PyWebDriverFramework submodule and install it and the
framework that the tests rely on (tfhw_main) into the local Python site-packages.

The setup script will then fetch the chromedriver and geckodriver binaries and place them in `drivers/`. This framework
requires that driver binaries be located in the PATH, so if there is not currently a chromedriver/geckodriver in
/usr/local/bin, the setup script will place them there. If there is, the script will report that you should delete them
manually if you would like to replace them.

The output of the setup script should look similar to the following:
<details><summary>Example Output:</summary>
<p>

```
[ check ] Checking prerequisites:
[ check ] curl...ok
[ check ] tar...ok
[ check ] unzip...ok
[ check ] python3...ok
[ check ] pip3...ok
[ check ] pytest...ok
Collecting selenium==3.6.0 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/48/90/29bcfa7ced2836016a400e8216e5a4166a71923b05d452ee7ee9e8775156/selenium-3.6.0-py2.py3-none-any.whl
Installing collected packages: selenium
Successfully installed selenium-3.6.0
Submodule 'PyWebDriverFramework' (git@github.com:dubszy/PyWebDriverFramework.git) registered for path 'PyWebDriverFramework'
Cloning into '<download_path>/true-fit-hw/PyWebDriverFramework'...
Submodule path 'PyWebDriverFramework': checked out '75e3ee774f50fefc799028a197b0084975d4db99'
<download_path>/true-fit-hw/PyWebDriverFramework ~/development/test/true-fit-hw
running install
running build
running build_py
creating build
creating build/lib
creating build/lib/wdframework
copying wdframework/store.py -> build/lib/wdframework
copying wdframework/selector.py -> build/lib/wdframework
copying wdframework/session.py -> build/lib/wdframework
copying wdframework/__init__.py -> build/lib/wdframework
copying wdframework/exceptions.py -> build/lib/wdframework
copying wdframework/driver_env.py -> build/lib/wdframework
creating build/lib/wdframework/loadables
copying wdframework/loadables/__init__.py -> build/lib/wdframework/loadables
copying wdframework/loadables/page.py -> build/lib/wdframework/loadables
copying wdframework/loadables/component.py -> build/lib/wdframework/loadables
copying wdframework/loadables/loadable.py -> build/lib/wdframework/loadables
running install_lib
creating /usr/local/lib/python3.7/site-packages/wdframework
copying build/lib/wdframework/store.py -> /usr/local/lib/python3.7/site-packages/wdframework
copying build/lib/wdframework/selector.py -> /usr/local/lib/python3.7/site-packages/wdframework
copying build/lib/wdframework/session.py -> /usr/local/lib/python3.7/site-packages/wdframework
copying build/lib/wdframework/__init__.py -> /usr/local/lib/python3.7/site-packages/wdframework
copying build/lib/wdframework/exceptions.py -> /usr/local/lib/python3.7/site-packages/wdframework
creating /usr/local/lib/python3.7/site-packages/wdframework/loadables
copying build/lib/wdframework/loadables/__init__.py -> /usr/local/lib/python3.7/site-packages/wdframework/loadables
copying build/lib/wdframework/loadables/page.py -> /usr/local/lib/python3.7/site-packages/wdframework/loadables
copying build/lib/wdframework/loadables/component.py -> /usr/local/lib/python3.7/site-packages/wdframework/loadables
copying build/lib/wdframework/loadables/loadable.py -> /usr/local/lib/python3.7/site-packages/wdframework/loadables
copying build/lib/wdframework/driver_env.py -> /usr/local/lib/python3.7/site-packages/wdframework
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/store.py to store.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/selector.py to selector.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/session.py to session.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/__init__.py to __init__.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/exceptions.py to exceptions.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/loadables/__init__.py to __init__.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/loadables/page.py to page.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/loadables/component.py to component.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/loadables/loadable.py to loadable.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/wdframework/driver_env.py to driver_env.cpython-37.pyc
running install_egg_info
Writing /usr/local/lib/python3.7/site-packages/PyWebDriverFramework-0.0.1-py3.7.egg-info
<download_path>/true-fit-hw
<download_path>/true-fit-hw/true_fit_hw ~/development/test/true-fit-hw
running install
running build
running build_py
creating build
creating build/lib
creating build/lib/tfhw_main
copying tfhw_main/__init__.py -> build/lib/tfhw_main
package init file 'tfhw_main/common/loadables/pageobjects/__init__.py' not found (or not a regular file)
creating build/lib/tfhw_main/common
creating build/lib/tfhw_main/common/loadables
creating build/lib/tfhw_main/common/loadables/pageobjects
copying tfhw_main/common/loadables/pageobjects/search_results_page.py -> build/lib/tfhw_main/common/loadables/pageobjects
copying tfhw_main/common/loadables/pageobjects/home_page.py -> build/lib/tfhw_main/common/loadables/pageobjects
package init file 'tfhw_main/common/loadables/pageobjects/__init__.py' not found (or not a regular file)
running install_lib
creating /usr/local/lib/python3.7/site-packages/tfhw_main
copying build/lib/tfhw_main/__init__.py -> /usr/local/lib/python3.7/site-packages/tfhw_main
creating /usr/local/lib/python3.7/site-packages/tfhw_main/common
creating /usr/local/lib/python3.7/site-packages/tfhw_main/common/loadables
creating /usr/local/lib/python3.7/site-packages/tfhw_main/common/loadables/pageobjects
copying build/lib/tfhw_main/common/loadables/pageobjects/search_results_page.py -> /usr/local/lib/python3.7/site-packages/tfhw_main/common/loadables/pageobjects
copying build/lib/tfhw_main/common/loadables/pageobjects/home_page.py -> /usr/local/lib/python3.7/site-packages/tfhw_main/common/loadables/pageobjects
byte-compiling /usr/local/lib/python3.7/site-packages/tfhw_main/__init__.py to __init__.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/tfhw_main/common/loadables/pageobjects/search_results_page.py to search_results_page.cpython-37.pyc
byte-compiling /usr/local/lib/python3.7/site-packages/tfhw_main/common/loadables/pageobjects/home_page.py to home_page.cpython-37.pyc
running install_egg_info
Writing /usr/local/lib/python3.7/site-packages/tfhw_main-0.0.1-py3.7.egg-info
<download_path>/true-fit-hw
<download_path>/true-fit-hw/drivers ~/development/test/true-fit-hw
Fetching chromedriver
Archive:  chromedriver.zip
  inflating: chromedriver
Fetching geckodriver
x geckodriver
<download_path>/true-fit-hw
Done!
```

</p>
</details>

## Running
After downloading and setting up the project, the Selenium tests can be run. The tests should be run with the following
command from `/path/to/download/true-fit-hw/true-fit-hw`:
```bash
python3 tests/smoke_tests/smoke_tests.py
```
The tests are run using Python's unittest, via the module `smoke_tests.py`.

## Test Structure
The tests are set up with one test in each test case, and one file per test case. This is to prevent tests from leaking
their state into other tests, as well as to keep the tests succinct and easily extendable, maintainable, movable, and
replaceable.
