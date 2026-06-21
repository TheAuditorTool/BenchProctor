# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest02561(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = default_blank(forwarded_ip)
    yaml.safe_load(data)
    return {"updated": True}
