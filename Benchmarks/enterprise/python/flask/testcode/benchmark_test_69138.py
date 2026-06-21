# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json


def BenchmarkTest69138():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
