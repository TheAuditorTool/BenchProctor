# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest04481():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(query_array)
    data = collected
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
