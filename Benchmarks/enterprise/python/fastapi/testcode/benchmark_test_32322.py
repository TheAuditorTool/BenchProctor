# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest32322(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    requests.get(str(data))
    return {"updated": True}
