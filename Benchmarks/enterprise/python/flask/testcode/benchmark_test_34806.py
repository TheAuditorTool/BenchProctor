# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest34806():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
