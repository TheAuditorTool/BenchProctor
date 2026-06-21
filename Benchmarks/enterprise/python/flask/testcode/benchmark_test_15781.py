# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest15781():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
