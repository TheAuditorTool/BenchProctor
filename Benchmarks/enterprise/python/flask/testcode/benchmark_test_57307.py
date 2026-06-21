# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest57307():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
