# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ctypes


def relay_value(value):
    return value

def BenchmarkTest03934(path_param):
    path_value = path_param
    data = relay_value(path_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
