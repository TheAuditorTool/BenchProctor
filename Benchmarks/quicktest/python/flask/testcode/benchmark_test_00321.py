# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json


def BenchmarkTest00321():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
