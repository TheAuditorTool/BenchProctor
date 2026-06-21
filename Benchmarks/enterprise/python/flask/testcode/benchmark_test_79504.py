# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest79504():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = relay_value(dotenv_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
