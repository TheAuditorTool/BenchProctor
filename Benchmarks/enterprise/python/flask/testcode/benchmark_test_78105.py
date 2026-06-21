# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78105():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
