# SPDX-License-Identifier: Apache-2.0
import logging
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest62721():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = unquote(query_array)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
