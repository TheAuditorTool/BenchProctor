# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest03125():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = '%s' % str(secret_value)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
