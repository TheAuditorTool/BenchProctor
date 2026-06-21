# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest49121():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    def normalize(value):
        return value.strip()
    data = normalize(query_array)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
