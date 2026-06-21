# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest65507():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    kind = 'json' if str(query_array).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = query_array
            data = parsed
        case _:
            data = query_array
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
