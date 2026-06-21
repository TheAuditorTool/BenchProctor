# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest21687():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
