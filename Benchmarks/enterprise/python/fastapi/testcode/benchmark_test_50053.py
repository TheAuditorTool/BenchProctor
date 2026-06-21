# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest50053(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
