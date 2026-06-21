# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest33826():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
