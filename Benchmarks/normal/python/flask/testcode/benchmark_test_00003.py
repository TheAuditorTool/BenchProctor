# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest00003():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
