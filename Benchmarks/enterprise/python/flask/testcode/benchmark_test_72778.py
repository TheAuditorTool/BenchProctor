# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest72778(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
