# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest06505(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    yaml.safe_load(data)
    return {"updated": True}
