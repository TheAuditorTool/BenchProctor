# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest63107():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = ' '.join(str(query_array).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
