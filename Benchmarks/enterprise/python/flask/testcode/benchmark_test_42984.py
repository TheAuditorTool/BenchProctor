# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest42984(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
