# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest46699():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
