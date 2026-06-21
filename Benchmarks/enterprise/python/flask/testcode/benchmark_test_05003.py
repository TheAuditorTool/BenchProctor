# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest05003():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ns = SimpleNamespace(payload=yaml_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
