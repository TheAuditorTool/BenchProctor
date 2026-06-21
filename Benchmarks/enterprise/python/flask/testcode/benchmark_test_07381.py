# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest07381():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    parts = []
    for token in str(query_array).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
