# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest06056(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return {"updated": True}
