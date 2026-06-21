# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest13263():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
