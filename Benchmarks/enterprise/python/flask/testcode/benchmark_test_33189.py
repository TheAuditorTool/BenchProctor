# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest33189():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
