# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest01215():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = '%s' % str(query_array)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
