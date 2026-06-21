# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import json


def BenchmarkTest50174():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    try:
        data = json.loads(query_array).get('value', query_array)
    except (json.JSONDecodeError, AttributeError):
        data = query_array
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
