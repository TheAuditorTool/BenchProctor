# SPDX-License-Identifier: Apache-2.0
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest11773():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
