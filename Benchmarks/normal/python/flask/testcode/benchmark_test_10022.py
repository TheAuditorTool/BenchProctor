# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest10022(path_param):
    path_value = path_param
    data = to_text(path_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
