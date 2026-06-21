# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest71083():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
