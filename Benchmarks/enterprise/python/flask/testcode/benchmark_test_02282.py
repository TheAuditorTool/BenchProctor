# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest02282():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
