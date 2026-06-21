# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest02037():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
