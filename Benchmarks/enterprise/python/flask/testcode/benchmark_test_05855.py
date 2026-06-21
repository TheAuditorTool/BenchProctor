# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest05855():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    if dotenv_value:
        data = dotenv_value
    else:
        data = ''
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
