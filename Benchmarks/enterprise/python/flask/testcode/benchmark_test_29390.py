# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest29390(path_param):
    path_value = path_param
    data = unquote(path_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
