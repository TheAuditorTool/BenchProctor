# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ctypes


def BenchmarkTest35853():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
