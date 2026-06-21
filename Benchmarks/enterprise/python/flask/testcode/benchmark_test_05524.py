# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest05524():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
