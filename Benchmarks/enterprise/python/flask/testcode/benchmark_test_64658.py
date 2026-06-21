# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os
from types import SimpleNamespace


def BenchmarkTest64658():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
