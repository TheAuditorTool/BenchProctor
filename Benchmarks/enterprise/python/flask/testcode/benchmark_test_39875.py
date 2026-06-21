# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest39875():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
