# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest12698():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
