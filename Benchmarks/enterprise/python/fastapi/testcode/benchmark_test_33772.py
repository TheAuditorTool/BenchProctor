# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest33772(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
