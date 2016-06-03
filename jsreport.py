#!/usr/bin/env python
"""
Helper script to pull data from https://www.justserve.org.
"""

def get_project_count(zipcode, radius="5", driver="firefox"):
    """
    Returns the number of projects on JustServe.org at the given zipcode,
    within the given radius.
    """
    pass




if __name__=='__main__':
    # Main entry point
    import argparse
    parser = argparse.ArgumentParser(
            description="Retrieve the number of JustServe projects at a zipcode.")
    parser.add_argument("-z", "--zipcode", required=True, 
            help="The five digit zipcode at the center of the search radius.")
    parser.add_argument("-r", "--radius", default="5",
            choices=["5", "10", "15", "25", "50", "75"],
            help="The search radius, in miles. Defaults to 5.")
    parser.add_argument("-d", "--driver", default="firefox",
            choices=["firefox", "chrome", "phantomjs", 
                "zope.testbrowser", "django"],
            help="The WebDriver to use. Defaults to firefox.")
    args = parser.parse_args()

