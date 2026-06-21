# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify
import json


def BenchmarkTest67939():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    try:
        data = json.loads(query_array).get('value', query_array)
    except (json.JSONDecodeError, AttributeError):
        data = query_array
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
