# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest10438(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
