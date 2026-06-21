# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04116():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
