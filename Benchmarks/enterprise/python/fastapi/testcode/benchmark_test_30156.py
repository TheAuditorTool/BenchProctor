# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest30156(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    requests.get(str(raw_body))
    return {"updated": True}
