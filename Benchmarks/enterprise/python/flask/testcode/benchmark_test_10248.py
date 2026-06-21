# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest10248(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
