# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest00833():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = (lambda v: v.strip())(secret_value)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
