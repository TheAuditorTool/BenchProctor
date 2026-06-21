# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64762():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
