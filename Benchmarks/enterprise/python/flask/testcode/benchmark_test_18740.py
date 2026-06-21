# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest18740():
    ua_value = request.headers.get('User-Agent', '')
    logging.info('User action: ' + str(ua_value))
    return jsonify({"result": "success"})
