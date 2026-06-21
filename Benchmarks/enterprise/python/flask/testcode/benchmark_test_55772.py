# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os
from types import SimpleNamespace


def BenchmarkTest55772(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
