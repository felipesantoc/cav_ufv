# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CAV
                                 A QGIS plugin
 cota area volume
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-01-19
        copyright            : (C) 2022 by JC
        email                : oliveirajc@ufv.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

# noinspection PyPep8Naming


def classFactory(iface):  # pylint: disable=invalid-name
    """Load CAV class from file CAV.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    import subprocess

    def instalar_biblioteca(biblioteca):
        try:
            # Tenta importar a biblioteca
            __import__(biblioteca)
        except ImportError:
            # Se não conseguir importar, instala a biblioteca usando o pip
            subprocess.call(['pip', 'install', biblioteca])
            print(f'Biblioteca {biblioteca} instalada com sucesso.')
        else:
            print(f'Biblioteca {biblioteca} já está instalada.')

        # Exemplo de uso
        bibliotecas_necessarias = ['numpy', 'matplotlib', 'reportlab', 'resources', 'sqlite3', 'pandas', 'processing']
        for biblioteca in bibliotecas_necessarias:
            instalar_biblioteca(biblioteca)

    from .CAV import CAV
    return CAV(iface)


import os.path
import processing
import os
import matplotlib.pyplot as plt
import numpy as np
def r2_score_manual(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2_score = 1 - (ss_res / ss_tot)
    return r2_score

import sys
plugin_path = os.path.dirname(__file__)
print('plugin_path =', plugin_path)
sys.path.append(os.path.join(os.path.join(plugin_path,'libs')))

import reportlab.lib.pagesizes as pagina
import sqlite3
import pandas as pd