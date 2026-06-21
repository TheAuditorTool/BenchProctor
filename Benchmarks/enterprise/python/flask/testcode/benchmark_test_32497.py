# SPDX-License-Identifier: Apache-2.0
import random
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest32497():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
