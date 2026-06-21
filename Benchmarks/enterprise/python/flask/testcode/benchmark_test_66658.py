# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest66658(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
