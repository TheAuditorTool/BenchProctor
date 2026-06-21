# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest24138():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
