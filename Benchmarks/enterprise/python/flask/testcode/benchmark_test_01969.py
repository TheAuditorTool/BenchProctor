# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01969():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
