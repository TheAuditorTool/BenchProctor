# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest52338(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
