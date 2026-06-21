# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import json


def BenchmarkTest07130(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
