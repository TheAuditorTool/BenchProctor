# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest10141(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    requests.get(str(data))
    return {"updated": True}
