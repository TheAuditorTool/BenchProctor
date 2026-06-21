# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest19700(request: Request, field: str = Form('')):
    field_value = field
    requests.post('https://api.prod.internal/data', data=str(field_value), verify=True)
    return {"updated": True}
