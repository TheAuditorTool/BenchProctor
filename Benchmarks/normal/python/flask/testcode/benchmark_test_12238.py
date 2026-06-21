# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest12238(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
