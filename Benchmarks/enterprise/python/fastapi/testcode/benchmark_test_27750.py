# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest27750(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    yaml.safe_load(data)
    return {"updated": True}
