# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest76498():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
