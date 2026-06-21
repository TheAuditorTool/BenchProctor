# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest03877(request: Request, field: str = Form('')):
    field_value = field
    requests.get(str(field_value))
    return {"updated": True}
