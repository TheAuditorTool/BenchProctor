# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest16637():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = []
    for token in str(dotenv_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
