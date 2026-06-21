# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest31151():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ns = SimpleNamespace(payload=config_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
