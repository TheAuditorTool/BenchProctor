# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest52112():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
