# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest34402():
    cookie_value = request.cookies.get('session_token', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(cookie_value),))
    logging.info('request processed')
    return jsonify({"result": "success"})
