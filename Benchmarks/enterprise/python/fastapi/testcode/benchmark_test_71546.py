# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest71546(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
