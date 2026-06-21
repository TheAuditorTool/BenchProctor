# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03131():
    host_value = request.headers.get('Host', '')
    data = default_blank(host_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
