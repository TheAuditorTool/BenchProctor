# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest64841(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    json.loads(data)
    return {"updated": True}
