# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest66759(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
