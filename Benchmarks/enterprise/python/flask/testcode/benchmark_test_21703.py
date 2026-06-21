# SPDX-License-Identifier: Apache-2.0
import logging
import base64
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest21703():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
