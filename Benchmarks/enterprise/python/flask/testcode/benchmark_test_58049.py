# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest58049(path_param):
    path_value = path_param
    data = default_blank(path_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
