# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest09720():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
