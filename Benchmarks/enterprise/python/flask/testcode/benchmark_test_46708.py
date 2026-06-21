# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest46708():
    secret_value = 'config_secret_test_abc123'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return jsonify({"result": "success"})
