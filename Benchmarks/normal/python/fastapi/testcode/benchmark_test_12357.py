# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def ensure_str(value):
    return str(value)

async def BenchmarkTest12357(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    yaml.safe_load(data)
    return {"updated": True}
