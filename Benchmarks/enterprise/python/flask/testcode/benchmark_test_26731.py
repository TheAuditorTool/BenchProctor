# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest26731():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
