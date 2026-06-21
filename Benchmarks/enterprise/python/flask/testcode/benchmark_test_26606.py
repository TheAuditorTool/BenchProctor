# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26606():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
