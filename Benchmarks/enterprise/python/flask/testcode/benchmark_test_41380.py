# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest41380():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
