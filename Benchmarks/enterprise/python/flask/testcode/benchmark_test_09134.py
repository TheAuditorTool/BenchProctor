# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest09134():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
