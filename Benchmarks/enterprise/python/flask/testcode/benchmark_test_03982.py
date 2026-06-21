# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest03982():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
