# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest66680():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
