# SPDX-License-Identifier: Apache-2.0
import logging
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest05252():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
