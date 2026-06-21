# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest57152():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
