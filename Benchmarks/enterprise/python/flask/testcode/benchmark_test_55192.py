# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest55192(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
