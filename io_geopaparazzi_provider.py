# -*- coding: utf-8 -*-

"""
/***************************************************************************
 IOGeopaparazzi
                                 A QGIS plugin
 A plugin to import/export geodata from/to geopaparazzi
                              -------------------
        begin                : 2017-02-27
        copyright            : (C) 2017 by Enrico A. Chiaradia
        email                : enrico.chiaradia@yahoo.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Enrico A. Chiaradia'
__date__ = '2017-02-27'
__copyright__ = '(C) 2017 by Enrico A. Chiaradia'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from import_gpap_algorithm import ImportGpapAlgorithm
from export_spatialite_algorithm import ExportSpatialiteAlgorithm
from export_tiles_algorithm import ExportTilesAlgorithm

import sys
import os.path as osp

from PyQt4.QtGui import *

#setting the path variable for icon
currentpath = osp.dirname(sys.modules[__name__].__file__)

class IOGeopaparazziProvider(AlgorithmProvider):

    MY_DUMMY_SETTING = 'MY_DUMMY_SETTING'

    def __init__(self):
        AlgorithmProvider.__init__(self)
        
        # Deactivate provider by default
        self.activate = False

        # Load algorithms
        self.alglist = [ImportGpapAlgorithm(),ExportSpatialiteAlgorithm(),ExportTilesAlgorithm()]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        """In this method we add settings needed to configure our
        provider.

        Do not forget to call the parent method, since it takes care
        or automatically adding a setting for activating or
        deactivating the algorithms in the provider.
        """
        AlgorithmProvider.initializeSettings(self)
        ProcessingConfig.addSetting(Setting('Example algorithms',
            IOGeopaparazziProvider.MY_DUMMY_SETTING,
            'Example setting', 'Default value'))

    def unload(self):
        """Setting should be removed here, so they do not appear anymore
        when the plugin is unloaded.
        """
        AlgorithmProvider.unload(self)
        ProcessingConfig.removeSetting(
            IOGeopaparazziProvider.MY_DUMMY_SETTING)

    def getName(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return 'IO Geopaparazzi'

    def getDescription(self):
        """This is the provired full name.
        """
        return 'Import/Export from/to Geopaparazzi'

    def getIcon(self):
        """We return the default icon.
        """
        return QIcon(osp.join(currentpath,'icons','IOGeopaparazzi.png'))

    def _loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        self.algs = self.alglist
