# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ctypes


def BenchmarkTest77020():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
