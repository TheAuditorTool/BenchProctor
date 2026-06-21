# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest27678():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
