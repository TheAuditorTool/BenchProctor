# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest58749():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    ns = SimpleNamespace(payload=query_array)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
