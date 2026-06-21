# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest04453():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
