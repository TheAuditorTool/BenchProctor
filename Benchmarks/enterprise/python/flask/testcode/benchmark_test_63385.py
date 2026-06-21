# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest63385():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
