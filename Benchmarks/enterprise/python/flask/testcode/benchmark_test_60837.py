# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest60837():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
