# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07771():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
