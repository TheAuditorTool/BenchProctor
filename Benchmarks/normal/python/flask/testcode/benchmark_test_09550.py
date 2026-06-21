# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest09550(path_param):
    path_value = path_param
    data = relay_value(path_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
