# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest71251(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = coalesce_blank(xml_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
