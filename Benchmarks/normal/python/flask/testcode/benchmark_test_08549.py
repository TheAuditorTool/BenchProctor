# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest08549(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
