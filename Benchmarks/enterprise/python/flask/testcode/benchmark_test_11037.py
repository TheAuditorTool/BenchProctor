# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest11037():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data, _sep, _rest = str(query_array).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
