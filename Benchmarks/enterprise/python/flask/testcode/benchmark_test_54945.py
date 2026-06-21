# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest54945():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
