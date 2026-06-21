# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ctypes


def BenchmarkTest76357():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
