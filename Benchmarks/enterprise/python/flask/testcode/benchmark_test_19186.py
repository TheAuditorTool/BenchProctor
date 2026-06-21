# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest19186():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
