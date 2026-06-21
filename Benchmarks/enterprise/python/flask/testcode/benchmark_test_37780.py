# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest37780(path_param):
    path_value = path_param
    data = relay_value(path_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
