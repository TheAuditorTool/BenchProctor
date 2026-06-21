# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json
import os


def BenchmarkTest43667():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
