# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest61111():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    ns = SimpleNamespace(payload=query_array)
    data = getattr(ns, 'payload')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
