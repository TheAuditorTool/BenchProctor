# SPDX-License-Identifier: Apache-2.0
import logging
import base64
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest04208():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
