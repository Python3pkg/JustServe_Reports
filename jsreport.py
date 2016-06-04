#!/usr/bin/env python
"""
Helper script to pull data from https://www.justserve.org.
"""
from selenium import webdriver


def get_project_count(zipcode, radius="5", driver="firefox"):
    """
    Returns the number of projects on JustServe.org at the given zipcode,
    within the given radius.
    """
    num_projects = "Not found"
    driver = webdriver.Chrome()
    driver.get('https://www.justserve.org')
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

