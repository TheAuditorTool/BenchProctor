# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13306():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
