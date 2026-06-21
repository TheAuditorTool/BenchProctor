# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os
from types import SimpleNamespace


def BenchmarkTest49440():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
