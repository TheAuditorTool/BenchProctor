# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest57000(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
