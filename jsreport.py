#!/usr/bin/env python
"""
Helper script to pull data from https://www.justserve.org.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pdb


def get_project_count(zipcode, radius="5", driver="firefox"):
    """
    Returns the number of projects on JustServe.org at the given zipcode,
    within the given radius.
    """
    num_projects = "0"
    driver = webdriver.Chrome()
    try:
        # Load the page
        driver.get('https://www.justserve.org')
        # search by zipcode
        zip_box = driver.find_element_by_css_selector("input.form__search__input")
        zip_box.send_keys(zipcode)
        # click Search
        search_btn = driver.find_element_by_css_selector("input.js-loadable")
        search_btn.click()
        # wait up to 10 seconds for the results
        # the ul appears to hold the search results, 
        # that is how we know the search is complete.
        wait_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "ul.js-flagstones")
            )
        )
        #pdb.set_trace()
        # Get the project count
        # Note, the html has several <small> tags with almost every option
        # of result (i.e. none found, etc). We want the one that is visible.
        smalls = driver.find_elements_by_css_selector("small.project-count")
        for e in smalls:
            if e.is_displayed():
                num_element = e.find_element_by_css_selector("span.project-count__num.ng-binding")
                num_projects = num_element.text
                break
    finally:
        driver.get_screenshot_as_file("%s.png" % zipcode)
        driver.quit()
    return num_projects




if __name__=='__main__':
    # Main entry point, when run as a script
    import argparse
    parser = argparse.ArgumentParser(
            description="Retrieve the number of JustServe projects at a zipcode.")
    parser.add_argument("zipcode", 
            help="The five digit zipcode at the center of the search radius.")
    parser.add_argument("-r", "--radius", default="5",
            choices=["5", "10", "15", "25", "50", "75"],
            help="The search radius, in miles. Defaults to 5.")
    parser.add_argument("-d", "--driver", default="firefox",
            choices=["firefox", "chrome", "phantomjs", 
                "zope.testbrowser", "django"],
            help="The WebDriver to use. Defaults to firefox.")
    args = parser.parse_args()
    project_count = get_project_count(args.zipcode, args.radius, args.driver)
    print "Projects:", project_count

