#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# data.py
# Copyright (c) 2020 Alvin(Xinyao) Sun <xinyao1@ualberta.ca>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import os


def readShortComplex(fileName, width=1):
    """Read binary data which in shortComplex '>i2' format

    Args:
        fileName (str): Path of the file
        width (int): Width of the data

    Example::

        >>> rslc = np.readShortComplex('sample.rslc', width=1)

    """
    return np.fromfile(fileName, '>i2').astype(np.float).view(np.complex).reshape(-1, width)


def readFloatComplex(fileName, width=1):
    """Read binary data which in floatCompoelx '>c8' format

    Args:
        fileName (str): Path of the file
        width (int): Width of the data
    """
    return np.fromfile(fileName, '>c8').astype(np.complex).reshape(-1, width)


def readFloat(fileName, width=1):
    """readFloat.

    Args:
        fileName (str): Path of the file
        width (int): Width of the data
    """
    return np.fromfile(fileName, '>f4').astype(np.float).reshape(-1, width)


def readBin(fileName, width, dataType, crop=None):
    """readBin.

    Args:
        fileName (str): Path of the file
        width (int): Width of the data
        dataType (string): 'floatComplex' | 'shortComplex' | 'float'
        crop List[int]: Crop information [crop_row, crop_col, crop_height, crop_width] 

    Returns:
        A numpy array of the data
    
    Example::

        Read RSLC in shortcomplex
        
        >>> full_rslc = readBin('example.rslc', width = 1000, dataType='shortComplex')
        >>> amp = np.abs(full_rslc)

        Read coherence in float
        >>> full_coh = readBin('example.filt.coh', width = 1000, dataType='float')

        Read a crop of interferogram in floatComplex
        >>> crop_filt = readBin('example.filt', width = 1000, dataType='floatComplex', crop=[100,200,300,300])
        >>> crop_amp = np.abs(crop_filt)
        >>> crop_phase = np.angle(crop_filt)

    """
    data_format = '>f4'
    numpy_data_format = np.float32
    unit_size = 4
    mid_numpy_data_format = np.float32

    if (dataType == 'floatComplex'):
        data_format = '>c8'
        numpy_data_format = np.complex
        unit_size = 8
    elif (dataType == 'shortComplex'):
        data_format = '>i2'
        numpy_data_format = np.complex
        unit_size = 4
    elif (dataType == 'float'):
        data_format = '>f4'
        numpy_data_format = np.float32
        unit_size = 4

    if (unit_size > 4):
        mid_numpy_data_format = np.complex

    size_of_file = os.path.getsize(fileName)
    height = int(size_of_file / unit_size / width)

    if (crop):
        [crop_row, crop_col, crop_height, crop_width] = crop
    else:
        crop_row, crop_col, crop_height, crop_width = 0, 0, height, width

    ret = np.zeros([crop_height, crop_width], dtype=numpy_data_format)

    with open(fileName, "rb") as fin:
        for row_idx in range(crop_height):
            fin.seek(unit_size * (width * (crop_row + row_idx)) + crop_col)
            ret[row_idx] = np.frombuffer(fin.read(unit_size * crop_width), dtype=data_format).astype(mid_numpy_data_format).view(numpy_data_format)
    return ret


def writeShortComplex(fileName, data):
    """Write numpy data into file '>i2' format

    Data will be flatten before writing to the file

    Args:
        fileName (str): Path of the file
        data (numpy_array): Numpy array
    """
    out_file = open(fileName, 'wb')
    data.copy().view(np.float).astype('>i2').tofile(out_file)
    out_file.close()


def writeFloatComplex(fileName, data):
    """writeFloatComplex.

    Args:
        fileName (str): Path of the file
        data (numpy_array): Numpy array
    """
    out_file = open(fileName, 'wb')
    data.astype('>c8').tofile(out_file)
    out_file.close()


def writeFloat(fileName, data):
    """writeFloat.

    Args:
        fileName (str): Path of the file
        data (numpy_array): Numpy array
    """
    out_file = open(fileName, 'wb')
    data.astype('>f4').tofile(out_file)
    out_file.close()
