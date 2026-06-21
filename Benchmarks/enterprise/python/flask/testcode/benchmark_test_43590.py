# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest43590(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
