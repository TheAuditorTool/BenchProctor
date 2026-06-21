# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest66114(path_param):
    path_value = path_param
    trusted_claim = str(path_value)
    return jsonify({'trusted': trusted_claim}), 200
