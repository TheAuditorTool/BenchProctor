# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest48751():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
