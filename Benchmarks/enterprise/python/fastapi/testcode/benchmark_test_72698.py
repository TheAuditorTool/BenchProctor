# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest72698(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
