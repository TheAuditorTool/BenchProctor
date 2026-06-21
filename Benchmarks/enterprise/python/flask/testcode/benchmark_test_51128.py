# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest51128():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = str(query_array).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
