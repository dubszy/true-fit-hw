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
- MacOS machine with curl, unzip, tar, Python 3.6, pip3, and pytest 3 installed.
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

The setup script will then fetch the chromedriver and geckodriver binaries and place them in `drivers/`.

The output of the setup script should look similar to the following:
```
[ check ] Checking prerequisites:
[ check ] curl...ok
[ check ] tar...ok
[ check ] unzip...ok
[ check ] python3...ok
[ check ] pip3...ok
[ check ] pytest...ok
Collecting selenium==3.6.0 (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/48/90/29bcfa7ced2836016a400e8216e5a4166a71923b05d452ee7ee9e8775156/selenium-3.6.0-py2.py3-none-any.whl (924kB)
    100% |████████████████████████████████| 931kB 8.6MB/s
Installing collected packages: selenium
~/development/true-fit-hw/drivers ~/development/true-fit-hw
Fetching chromedriver
Archive:  chromedriver.zip
  inflating: chromedriver
Fetching geckodriver
x geckodriver
<download_directory>/true-fit-hw
Done!
```

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
