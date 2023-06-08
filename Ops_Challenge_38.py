#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Date:        TODO: 06/08/2023
# Modified by: TODO: Tyler Housden

#utilized chatgpt

### TODO: Install requests bs4 before executing this in Python3
### Install the required libraries using the following command:
### pip install requests beautifulsoup4

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###
### The get_all_forms function retrieves all the HTML form elements from a given URL.
### It uses the requests library to get the web page content and BeautifulSoup to parse the HTML.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### TODO: Add function explanation here ###
### The get_form_details function takes a form element and extracts its action, method, and input fields.
### It returns a dictionary containing the form details.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### TODO: Add function explanation here ###
### The submit_form function takes the form details, URL, and a value to be submitted in the form.
### It constructs the form data and performs a POST or GET request to submit the form.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### TODO: Add function explanation here ###
### The scan_xss function scans a given URL for XSS vulnerabilities.
### It detects all the forms on the page, submits a JavaScript payload, and checks if the payload is reflected in the response.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<script>alert("XSS Vulnerability")</script>'
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### TODO: Add main explanation here ###
### The main function is the entry point of the script.
### It prompts the user to enter a URL to test for XSS vulnerabilities, calls the scan_xss function, and prints the result.
if
