# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest60654():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
