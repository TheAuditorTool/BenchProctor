# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest78302():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = query_array if query_array else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
