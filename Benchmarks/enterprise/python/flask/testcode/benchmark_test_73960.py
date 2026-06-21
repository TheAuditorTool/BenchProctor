# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest73960():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    return str(data), 200, {'Content-Type': 'text/html'}
