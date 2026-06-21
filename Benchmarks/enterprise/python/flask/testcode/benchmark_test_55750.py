# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest55750():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
