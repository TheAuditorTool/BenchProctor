# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest45838(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
