# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest42887():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
