# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest75895():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
