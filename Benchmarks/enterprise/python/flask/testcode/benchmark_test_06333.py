# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest06333():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
