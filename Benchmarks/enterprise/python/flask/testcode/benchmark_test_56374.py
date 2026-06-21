# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest56374(path_param):
    path_value = path_param
    data = f'{path_value}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
