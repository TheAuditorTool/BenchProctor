# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest60194():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
