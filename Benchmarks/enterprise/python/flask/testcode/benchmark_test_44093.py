# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest44093():
    cookie_value = request.cookies.get('session_token', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(cookie_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(cookie_value))
    return jsonify({"result": "success"})
