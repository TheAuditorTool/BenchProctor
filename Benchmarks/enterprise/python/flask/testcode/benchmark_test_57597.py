# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest57597():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
