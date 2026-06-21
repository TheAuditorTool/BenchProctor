# SPDX-License-Identifier: Apache-2.0
import json
from flask import request


def BenchmarkTest78793():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
