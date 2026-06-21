# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest38132():
    header_value = request.headers.get('X-Custom-Header', '')
    logging.info('User action: ' + str(header_value))
    return jsonify({"result": "success"})
