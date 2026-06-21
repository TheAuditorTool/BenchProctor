# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest42144():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
