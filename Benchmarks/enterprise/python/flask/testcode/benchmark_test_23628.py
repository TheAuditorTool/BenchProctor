# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest23628():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
