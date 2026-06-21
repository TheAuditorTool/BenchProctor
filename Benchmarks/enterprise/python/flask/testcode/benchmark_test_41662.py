# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest41662(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
