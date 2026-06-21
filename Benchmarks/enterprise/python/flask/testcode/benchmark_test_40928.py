# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest40928():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(graphql_var),))
    return jsonify({"result": "success"})
