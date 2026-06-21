# SPDX-License-Identifier: Apache-2.0
import logging
import base64
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest48193():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
