# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest62988():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return jsonify({"result": "success"})
