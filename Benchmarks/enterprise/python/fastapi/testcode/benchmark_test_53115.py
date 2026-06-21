# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest53115(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    requests.get(str(data))
    return {"updated": True}
