# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest66282():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
