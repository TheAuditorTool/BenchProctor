# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest48742():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if not auth_check(session.get('user', ''), str(graphql_var)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
