# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest41726(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    requests.get(str(data))
    return {"updated": True}
