# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes
from types import SimpleNamespace


def BenchmarkTest08067():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
