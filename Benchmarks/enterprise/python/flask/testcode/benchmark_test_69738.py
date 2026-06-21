# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest69738():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
