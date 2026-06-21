# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03936():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    processed = 'true' if str(graphql_var).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})
