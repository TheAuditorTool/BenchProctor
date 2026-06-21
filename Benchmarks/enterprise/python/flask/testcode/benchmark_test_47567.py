# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest47567():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
