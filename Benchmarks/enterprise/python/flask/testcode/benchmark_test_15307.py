# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15307():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
