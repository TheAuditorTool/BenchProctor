# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest47163():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
