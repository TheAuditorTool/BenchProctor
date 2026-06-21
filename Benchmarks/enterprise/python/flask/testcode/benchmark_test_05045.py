# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ctypes
from types import SimpleNamespace


def BenchmarkTest05045():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
