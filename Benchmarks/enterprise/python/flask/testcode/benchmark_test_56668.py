# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest56668():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
