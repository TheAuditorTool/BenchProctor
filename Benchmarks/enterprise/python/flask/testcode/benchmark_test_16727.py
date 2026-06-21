# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest16727():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
