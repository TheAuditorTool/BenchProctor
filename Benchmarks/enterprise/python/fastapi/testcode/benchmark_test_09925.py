# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest09925(request: Request):
    origin_value = request.headers.get('origin', '')
    requests.get(str(origin_value))
    return {"updated": True}
