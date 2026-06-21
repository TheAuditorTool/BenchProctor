# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest44560():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
