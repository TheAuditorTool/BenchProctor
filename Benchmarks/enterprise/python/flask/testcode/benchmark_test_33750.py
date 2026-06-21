# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest33750():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
