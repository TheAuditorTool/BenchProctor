# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ctypes


def to_text(value):
    return str(value).strip()

def BenchmarkTest66020():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
