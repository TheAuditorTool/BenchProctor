# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest31495():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    def normalize(value):
        return value.strip()
    data = normalize(dotenv_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
