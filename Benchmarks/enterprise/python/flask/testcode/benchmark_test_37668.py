# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest37668():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
