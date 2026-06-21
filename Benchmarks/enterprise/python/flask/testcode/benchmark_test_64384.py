# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest64384():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data, _sep, _rest = str(secret_value).partition('\x00')
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
