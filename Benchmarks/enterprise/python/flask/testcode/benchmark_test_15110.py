# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15110():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
