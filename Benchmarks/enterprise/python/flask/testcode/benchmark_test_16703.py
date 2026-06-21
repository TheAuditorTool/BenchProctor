# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest16703():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(dotenv_value)
    data = collected
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
