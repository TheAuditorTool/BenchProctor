# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest50795():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
