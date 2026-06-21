# SPDX-License-Identifier: Apache-2.0
import logging
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest36663():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
