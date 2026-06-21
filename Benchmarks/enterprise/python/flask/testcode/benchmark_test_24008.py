# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24008():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
