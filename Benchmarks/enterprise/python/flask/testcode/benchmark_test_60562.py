# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest60562():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    kind = 'json' if str(query_array).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = query_array
            data = parsed
        case _:
            data = query_array
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
