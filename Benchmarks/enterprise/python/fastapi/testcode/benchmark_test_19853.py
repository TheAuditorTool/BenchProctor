# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest19853(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
