# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json


def BenchmarkTest05950():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
