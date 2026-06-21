# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest15150():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
