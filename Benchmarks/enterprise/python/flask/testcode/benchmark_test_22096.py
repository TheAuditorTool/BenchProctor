# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json


def BenchmarkTest22096():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
