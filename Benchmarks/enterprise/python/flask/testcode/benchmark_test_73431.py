# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest73431(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
