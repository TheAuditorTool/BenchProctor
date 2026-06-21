# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


def normalise_input(value):
    return value.strip()

async def BenchmarkTest73830(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
