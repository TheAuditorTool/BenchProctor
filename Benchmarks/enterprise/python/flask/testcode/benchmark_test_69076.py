# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest69076():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    return str(data), 200, {'Content-Type': 'text/html'}
