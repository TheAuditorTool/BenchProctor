# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ctypes


def BenchmarkTest05622():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
