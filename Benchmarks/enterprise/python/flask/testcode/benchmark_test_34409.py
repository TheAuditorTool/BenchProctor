# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest34409():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
