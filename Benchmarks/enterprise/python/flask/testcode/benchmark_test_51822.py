# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest51822(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
