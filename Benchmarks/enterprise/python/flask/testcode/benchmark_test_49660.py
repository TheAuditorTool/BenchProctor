# SPDX-License-Identifier: Apache-2.0
import logging
import json
from flask import request, jsonify


def BenchmarkTest49660():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
