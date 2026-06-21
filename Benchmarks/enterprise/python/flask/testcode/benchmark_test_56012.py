# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest56012():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ns = SimpleNamespace(payload=prop_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
