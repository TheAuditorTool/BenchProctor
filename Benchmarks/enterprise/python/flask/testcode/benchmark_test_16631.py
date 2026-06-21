# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest16631():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    parts = []
    for token in str(query_array).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
