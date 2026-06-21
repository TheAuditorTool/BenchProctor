# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json


def BenchmarkTest20243():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
