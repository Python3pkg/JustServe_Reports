#!/usr/bin/env python
"""
Helper script to pull data from https://www.justserve.org.
"""
from splinter import Browser


def get_project_count(zipcode, radius="5", driver="firefox"):
    """
    Returns the number of projects on JustServe.org at the given zipcode,
    within the given radius.
    """
    num_projects = "Not found"
    with Browser(driver) as browser:
        browser.visit('https://www.justserve.org/')
        browser.screenshot("1.png")
        search_box = browser.find_by_css("input.form__search__input").first
        search_box.fill(zipcode)
        #browser.find_by_css("a.js-toggle-form-filters").first.click()
        
        #radius_select = browser.find_by_css("select.js-miles").first
        #radius_select.click()
        #radius_select.select(radius)
        #browser.select("js-miles", radius)
        #browser.find_option_by_text("%s miles" % radius).first.click()
        #for option in radius_select.find_by_tag("option"):
        #    if option.value == radius:
        #        option.click()
        #        break

        #browser.find_by_css("input.js-loadable").first.click()
        browser.screenshot("2.png")
        #btn = browser.find_by_css("input.js-loadable").first
        #browser.execute_script("arguments[0].click();", btn)
        
        #num_projects = browser.find_by_css("project-count__num").first.value
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

