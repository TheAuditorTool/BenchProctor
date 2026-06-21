# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest77161():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
