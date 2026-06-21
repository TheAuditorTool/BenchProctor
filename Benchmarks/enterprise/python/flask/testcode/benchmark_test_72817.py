# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72817():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
