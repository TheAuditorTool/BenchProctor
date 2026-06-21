# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest21286():
    host_value = request.headers.get('Host', '')
    logging.info('User action: ' + str(host_value))
    return jsonify({"result": "success"})
