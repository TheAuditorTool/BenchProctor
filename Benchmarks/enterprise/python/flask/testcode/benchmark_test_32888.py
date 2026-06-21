# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes
from types import SimpleNamespace


def BenchmarkTest32888():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
