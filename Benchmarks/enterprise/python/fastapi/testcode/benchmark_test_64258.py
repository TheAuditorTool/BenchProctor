# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from fastapi import Form


async def BenchmarkTest64258(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    json.loads(data)
    return {"updated": True}
