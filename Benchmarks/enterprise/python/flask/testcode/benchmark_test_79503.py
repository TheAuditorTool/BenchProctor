# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest79503():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(graphql_var),))
    logging.info('audit actor=%s action=revoke_sessions', str(graphql_var))
    return jsonify({"result": "success"})
