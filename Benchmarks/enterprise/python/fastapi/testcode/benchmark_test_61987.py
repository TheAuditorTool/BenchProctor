# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest61987(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    yaml.safe_load(data)
    return {"updated": True}
