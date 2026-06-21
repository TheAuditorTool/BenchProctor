# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest22085(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    _resp = requests.get(str(header_value))
    exec(_resp.text)
    return {"updated": True}
