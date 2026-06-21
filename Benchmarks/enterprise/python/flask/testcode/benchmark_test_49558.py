# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest49558():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    logging.info('User action: ' + str(forwarded_ip))
    return jsonify({"result": "success"})
