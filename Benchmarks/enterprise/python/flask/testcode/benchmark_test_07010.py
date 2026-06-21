# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07010():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
