# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest33226(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
