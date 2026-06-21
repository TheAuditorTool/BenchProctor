# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest46380(request: Request, field: str = Form('')):
    field_value = field
    requests.post('http://api.prod.internal/data', data=str(field_value))
    return {"updated": True}
