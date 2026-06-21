# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest43865():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
