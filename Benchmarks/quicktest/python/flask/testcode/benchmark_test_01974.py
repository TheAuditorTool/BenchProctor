# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest01974():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
