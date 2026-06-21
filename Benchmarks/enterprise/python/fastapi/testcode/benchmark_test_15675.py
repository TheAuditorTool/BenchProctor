# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest15675(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    requests.get(str(header_value))
    return {"updated": True}
