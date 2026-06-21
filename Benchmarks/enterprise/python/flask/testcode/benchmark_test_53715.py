# SPDX-License-Identifier: Apache-2.0
import logging
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest53715():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
