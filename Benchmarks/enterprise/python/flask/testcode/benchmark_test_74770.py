# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


def BenchmarkTest74770():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '{}'.format(dotenv_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
