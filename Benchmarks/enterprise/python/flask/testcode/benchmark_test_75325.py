# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest75325(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
