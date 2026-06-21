# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def relay_value(value):
    return value

async def BenchmarkTest00286(request: Request):
    origin_value = request.headers.get('origin', '')
    data = relay_value(origin_value)
    yaml.safe_load(data)
    return {"updated": True}
