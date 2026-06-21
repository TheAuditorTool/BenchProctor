# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest75545():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    prefix = ''
    data = prefix + str(dotenv_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
