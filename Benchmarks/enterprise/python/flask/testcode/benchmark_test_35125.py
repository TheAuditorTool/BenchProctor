# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest35125():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = unquote(query_array)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
