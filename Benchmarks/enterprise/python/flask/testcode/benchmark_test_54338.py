# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest54338():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
