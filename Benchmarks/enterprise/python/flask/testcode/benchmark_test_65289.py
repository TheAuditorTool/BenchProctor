# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest65289():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
