# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest53409(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    requests.get(str(data))
    return {"updated": True}
