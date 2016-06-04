#!/usr/bin/env python
"""
Helper script to pull data from https://www.justserve.org.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_project_count(zipcode, radius="5", driver="firefox"):
    """
    Returns the number of projects on JustServe.org at the given zipcode,
    within the given radius.
    """
    num_projects = "Not found"
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.justserve.org')
        zip_box = driver.find_element_by_css_selector("input.form__search__input")
        zip_box.send_keys(zipcode)
        search_btn = driver.find_element_by_css_selector("input.js-loadable")
        search_btn.click()
        # wait up to 10 seconds for the results
        wait_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                #(By.CSS_SELECTOR, "span.project-count__num.ng-binding")
                #(By.CSS_SELECTOR, "small.project-count")
                (By.CSS_SELECTOR, "ul.js-flagstones")
            )
        )
        results_element = driver.find_element_by_css_selector("span.project-count__num.ng-binding")
        num_projects = results_element.text
    finally:
        driver.get_screenshot_as_file("%s.png" % zipcode)
        driver.quit()
    return num_projects




if __name__=='__main__':
    # Main entry point
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

