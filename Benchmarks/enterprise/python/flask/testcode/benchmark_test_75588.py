# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest75588():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
