# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest11178():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    pending = list(str(dotenv_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
