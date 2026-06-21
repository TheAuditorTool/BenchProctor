# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest18761():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = f'{query_array:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
