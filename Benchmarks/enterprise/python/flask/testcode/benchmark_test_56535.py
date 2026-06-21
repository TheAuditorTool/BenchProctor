# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest56535():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
