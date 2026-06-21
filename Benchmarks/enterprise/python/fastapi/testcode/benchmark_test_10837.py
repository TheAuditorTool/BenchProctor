# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest10837(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = coalesce_blank(raw_body)
    yaml.safe_load(data)
    return {"updated": True}
