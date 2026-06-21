# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest81449():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
