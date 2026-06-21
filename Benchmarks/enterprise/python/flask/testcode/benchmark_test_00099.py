# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest00099():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
