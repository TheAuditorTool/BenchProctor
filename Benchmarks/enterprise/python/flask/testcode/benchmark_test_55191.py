# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest55191():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
