#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     Interact with USGS website to retrieve data for structural simulations
#
# Author:      Holly Tina Ferguson hfergus2@nd.edu
#
# Created:     06/25/2017
# Copyright:   (c) Holly Tina Ferguson June 2017
# License:     The University of Notre Dame


# Download project from: https://github.com/usgs/nshmp-haz
# Get and Install to run it https://github.com/usgs/nshmp-haz/wiki/Building-&-Running
# You must do these steps to build a .jar locally to run the application under that tool: https://github.com/usgs/nshmp-haz/wiki/Building-&-Running
# Curves are built for the set of test locations we are using
# -------------------------------------------------------------------------------


import os
import sys
import urllib
import urllib2
import subprocess

def main(argv, inputfile='https://earthquake.usgs.gov/hazards/interactive/'):

    print "Main Started"
    run_flag = 1  # 0 for test runs and 1 for the actual curves the orchestration program needs

    # Access and Run nshmp-haz Tool                "Test Site, -122.0, 38.0"
    hazard = "java -cp dist\\nshmp-haz.jar org.opensha2.HazardCalc " #half of the hazard function terminal call. DO NOT USE IN ISOLATION
    if run_flag == 0:
        try:
            results = subprocess.call(hazard + ' etc\\peer\\models\\Set1-Case1 \"Test Site, -122.0, 38.0\"', shell=True) # simple example
        except:
            print "Error with simple call :("
            pass
        try:
            results = subprocess.call(hazard + 'etc\\peer\\models\\Set1-Case1 \"San Francisco, -122.40, 37.75\" config.json',shell=True)# complicated config file
        except:
            print "Error with complicated call :("
            pass
    if run_flag == 1:
        # try:
        #     results = subprocess.call(hazard + 'nshmp-model-cous-2008-master\\WesternUS sitesW.geojson config.json',shell=True)
        # except:
        #     print "Error with Cities on West side of US :("
        #     pass
        try:
            results = subprocess.call(hazard + 'nshmp-model-cous-2008-master\\CentralEastUS sitesE.geojson config.json',shell=True)
        except:
            print "Error with Cities on Central/East side of US :("
            pass


    print "Main Finished"

if __name__ == "__main__":
    main(sys.argv[1:])




























