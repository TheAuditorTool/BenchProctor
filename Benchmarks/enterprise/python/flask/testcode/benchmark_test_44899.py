# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest44899():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(json_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(json_value))
    return jsonify({"result": "success"})
