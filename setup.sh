#!/usr/bin/env bash

# Variables we'll need throughout this script
chromedriver="chromedriver"
geckodriver="geckodriver"
chromedriver_zip="$chromedriver.zip"
geckodriver_tar="$geckodriver.tar.gz"

function ok() {
    printf "\033[32mok\033[0m\n"
}

function error() {
    printf "\033[31merror\033[0m\n"
    exit 1
}

# Fetch chromedriver archive and extract it
function fetch_chromedriver() {
    printf "Fetching chromedriver\n"
    curl -fsSL -o "$chromedriver_zip" https://chromedriver.storage.googleapis.com/2.44/chromedriver_mac64.zip \
    && unzip -n "$chromedriver_zip" \
    && rm "$chromedriver_zip"

    if [[ -e "/usr/local/bin/$chromedriver" ]]; then
        printf "$chromedriver already installed in /usr/local/bin, please delete it manually to install the new one\n"
    else
        cp "$chromedriver" /usr/local/bin
    fi
}

# Fetch geckodriver archive and extract it
function fetch_geckodriver() {
    printf "Fetching geckodriver\n"
    curl -fsSL -o "$geckodriver_tar" https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-macos.tar.gz \
    && tar xzvkf "$geckodriver_tar" \
    && rm "$geckodriver_tar"

    if [[ -e "/usr/local/bin/$geckodriver" ]]; then
        printf "$geckodriver already installed in /usr/local/bin, please delete it manually to install the new one\n"
    else
        cp "$geckodriver" /usr/local/bin
    fi
}

# Checks for curl, tar and unzip
printf "[ check ] Checking prerequisites:\n"
printf "[ check ] curl..."; [[ -z `which curl` ]] && error || ok
printf "[ check ] tar..."; [[ -z `which tar` ]] && error || ok
printf "[ check ] unzip..."; [[ -z `which unzip` ]] && error || ok
printf "[ check ] python3..."; [[ -z `python3 --version | grep -e "3[.][67][.][0-9]"` ]] && error || ok
printf "[ check ] pip3..."; [[ -z `which pip3` ]] && error || ok
printf "[ check ] pytest..."; [[ -z `which pytest` ]] && error || ok

# Install requirements
pip3 install --user -r requirements.txt

# Fetch PyWebDriverFramework and install it
git submodule update --init \
&& pushd PyWebDriverFramework \
&& python3 setup.py install \
&& popd

# Install the framework that the tests will use
pushd true_fit_hw \
&& python3 setup.py install \
&& popd


### Install the WebDriver binaries ###

pushd drivers

# If this script was interrupted on the last run, these archives may not be gone, so toss them if they exist
[[ -e "$chromedriver_zip" ]] && rm "$chromedriver_zip"
[[ -e "$geckodriver_tar" ]] && rm "$geckodriver_tar"

# Check for existing chromedriver
if [[ -e "$chromedriver" ]]; then
    if [[ "$1" == "-f" ]]; then
        printf "Removing existing chromedriver\n"
        rm "$chromedriver" \
        && fetch_chromedriver
    else
        printf "chromedriver already exists, run this script with -f to remove existing drivers\n"
        exit 1
    fi
else
    fetch_chromedriver
fi

# Check for existing geckodriver
if [[ -e "$geckodriver" ]]; then
    if [[ "$1" == "-f" ]]; then
        printf "Removing existing geckodriver\n"
        rm "$geckodriver" \
        && fetch_geckodriver
    else
        printf "geckodriver already exists, run this script with -f to remove existing drivers\n"
        exit 1
    fi
else
    fetch_geckodriver
fi

chmod +x "$chromedriver" "$geckodriver"

popd

printf "\033[32mDone!\033[0m\n"
