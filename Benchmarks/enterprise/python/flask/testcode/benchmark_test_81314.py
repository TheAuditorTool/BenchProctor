# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest81314():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
