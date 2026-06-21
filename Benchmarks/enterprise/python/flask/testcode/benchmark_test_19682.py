# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest19682():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = (lambda v: v.strip())(dotenv_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
