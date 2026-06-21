# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest48738():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
