# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest23776():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    if query_array:
        data = query_array
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
