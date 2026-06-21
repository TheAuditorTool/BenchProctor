# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest00366():
    auth_header = request.headers.get('Authorization', '')
    logging.info('User action: ' + str(auth_header))
    return jsonify({"result": "success"})
