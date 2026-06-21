# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest15482():
    referer_value = request.headers.get('Referer', '')
    logging.info('User action: ' + str(referer_value))
    return jsonify({"result": "success"})
