# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest71025():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    pending = list(str(query_array).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
