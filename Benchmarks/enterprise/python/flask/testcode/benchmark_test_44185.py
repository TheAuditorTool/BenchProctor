# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest44185():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    base_name = os.path.basename(str(graphql_var))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
