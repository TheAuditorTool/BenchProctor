# SPDX-License-Identifier: Apache-2.0
import logging
import base64
from flask import request, jsonify


def BenchmarkTest67425():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
