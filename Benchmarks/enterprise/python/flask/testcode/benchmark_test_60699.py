# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest60699():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data, _sep, _rest = str(dotenv_value).partition('\x00')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
