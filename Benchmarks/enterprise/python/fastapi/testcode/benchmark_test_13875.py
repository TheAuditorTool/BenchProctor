# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest13875(request: Request):
    auth_header = request.headers.get('authorization', '')
    requests.get(str(auth_header))
    return {"updated": True}
