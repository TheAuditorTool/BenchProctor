# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest56561():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    session['user'] = str(data)
    return jsonify({"result": "success"})
