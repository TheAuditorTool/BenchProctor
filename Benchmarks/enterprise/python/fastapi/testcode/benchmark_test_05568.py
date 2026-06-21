# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest05568(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    requests.get(str(data))
    return {"updated": True}
