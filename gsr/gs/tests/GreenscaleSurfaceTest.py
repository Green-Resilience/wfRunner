#-------------------------------------------------------------------------------
# Name:        GreenscaleSurfaceTest.py
# Purpose:     Green Scale Tool UnitTests (GS EE surface level test)
#
# Author:      Holly Tina Ferguson
#
# Created:     15/09/2013
# Copyright:   (c) Holly Tina Ferguson 2013
# Licence:     The University of Notre Dame
#-------------------------------------------------------------------------------
import unittest
import os
from objects.GreenscaleSurface import GreenscaleSurface
#from GreenScaleV1 import GreenScaleV1
from gbXML import gbXML
from objects.Area import Area


class GreenscaleSurfaceTest(unittest.TestCase):
    # Again, resulsts test the function of the code, and not the actual values until the DB has proper material values

    def setUp(self):
        self.gbxml = gbXML(os.path.join(os.path.dirname(__file__), 'input/Single_model.xml'))
        #self.gbxml = gbXML(os.path.join(os.path.dirname(__file__), 'input/Two_Room_One_Floor_Model.xml'))

        area = Area()
        area.createAreaDictionary()
        area.createWinAreaDictionary()
        self.areaWinDict = area.getWinDictionary()
        self.areaDict = area.getDictionary()

        #self.db = GreenScaleV1(os.path.join(os.path.dirname(__file__), '..\objects'))
        self.db = os.path.join(os.path.dirname(__file__), '..\objects')

        #self.db.db_file = 'GreenScaleDBcsv.csv'
        self.EEsurface = GreenscaleSurface()

        # Get the first surface to check:
        spaces = self.gbxml.get_spaces()
        # Space 1 info, surface "su-8" is [7] and is the interior shared wall here
        space1 = spaces[0]
        surfaces = spaces[0].surfaces
        self.surface1 = surfaces[0]  # Ext. Wall with window
        self.surface2 = surfaces[1]  # Ext. Wall no openings
        self.surface3 = surfaces[2]  # Ext. Wall with window
        self.surface4 = surfaces[3]  # Ext. Wall with Door
        self.surface5 = surfaces[4]  # Roof
        self.surface6 = surfaces[5]  # Floor


    def test_calculate_surfaceEE(self):
        # Adding these as they are calculating, to be checked for accuracy later for the single model
        h_surface = 10  # This may need re-checking
        assembly = dict()
        assembly_descript = dict()

        sur = self.EEsurface.calculate_surfaceEE(self.db, self.surface1, assembly, assembly_descript, self.areaDict, self.areaWinDict, h_surface)
        self.assertEqual(sur, [25440847.355398998, 7097.9964119999995], 'Surface 1 EE and EW:  - %s ' % sur)

        sur = self.EEsurface.calculate_surfaceEE(self.db, self.surface2, assembly, assembly_descript, self.areaDict, self.areaWinDict, h_surface)
        self.assertEqual(sur, [13367883.422991, 3729.639475], 'Surface 2 EE and EW:  - %s ' % sur)

        sur = self.EEsurface.calculate_surfaceEE(self.db, self.surface3, assembly, assembly_descript, self.areaDict, self.areaWinDict, h_surface)
        self.assertEqual(sur, [25440847.355398998, 7097.9964119999995], 'Surface 3 EE and EW:  - %s ' % sur)

        sur = self.EEsurface.calculate_surfaceEE(self.db, self.surface4, assembly, assembly_descript, self.areaDict, self.areaWinDict, h_surface)
        self.assertEqual(sur, [11752126.191331001, 3278.843207], 'Surface 4 EE and EW:  - %s ' % sur)

        sur = self.EEsurface.calculate_surfaceEE(self.db, self.surface5, assembly, assembly_descript, self.areaDict, self.areaWinDict, h_surface)
        self.assertEqual(sur, [8481390.962298, 2366.308078], 'Surface 5 EE and EW:  - %s ' % sur)

        sur = self.EEsurface.calculate_surfaceEE(self.db, self.surface6, assembly, assembly_descript, self.areaDict, self.areaWinDict, h_surface)
        self.assertEqual(sur, [7819594.36063, 2181.666827], 'Surface 6 EE and EW:  - %s ' % sur)




