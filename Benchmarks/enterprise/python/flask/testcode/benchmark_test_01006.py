# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest01006():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
