# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ctypes


def BenchmarkTest48374(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
