# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest41617():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
