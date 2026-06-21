# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest36965(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    json.loads(data)
    return {"updated": True}
