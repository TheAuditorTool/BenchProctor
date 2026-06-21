# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest58393():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
