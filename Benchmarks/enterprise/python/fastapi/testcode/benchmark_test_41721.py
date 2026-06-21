# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest41721(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    requests.get(str(data))
    return {"updated": True}
