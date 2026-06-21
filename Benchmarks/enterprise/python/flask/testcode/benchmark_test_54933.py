# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest54933():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
