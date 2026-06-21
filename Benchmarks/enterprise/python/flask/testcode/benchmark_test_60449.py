# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60449():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
