# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10488():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
