# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CatchmentTool
               A QGIS plugin
 Calculates catchments
 ***************************************************************************/
"""

__author__ = 'Masawe , TANROADS Dodoma Tanzania'
__date__ = '2026-10-19'
__copyright__ = '(C) 2026 by Masawe , TANROADS Dodoma Tanzania'

import os
from qgis.core import QgsProcessingProvider, QgsApplication
from .catchment_tool import CatchmentTool


class CatchmentToolProvider(QgsProcessingProvider):
    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(CatchmentTool())

    def id(self):
        return 'catchment_tool'

    def name(self):
        return 'NEXT GEN'

    def icon(self):
        return QgsProcessingProvider.icon(self)


class CatchmentToolPlugin(object):

    def __init__(self, iface):
        self.iface = iface
        self.provider = None

    def initProcessing(self):
        self.provider = CatchmentToolProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        if self.provider:
            QgsApplication.processingRegistry().removeProvider(self.provider)


def classFactory(iface):
    """Load CatchmentToolPlugin from file __init__.py."""
    return CatchmentToolPlugin(iface)