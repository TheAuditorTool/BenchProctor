# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest55125():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
