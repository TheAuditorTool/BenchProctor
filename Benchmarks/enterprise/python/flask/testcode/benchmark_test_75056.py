# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75056():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    eval(str(data))
    return jsonify({"result": "success"})
