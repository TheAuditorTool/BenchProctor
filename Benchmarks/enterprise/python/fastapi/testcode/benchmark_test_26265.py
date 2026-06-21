# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest26265(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    requests.get(str(data))
    return {"updated": True}
