# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest39552(request: Request):
    ua_value = request.headers.get('user-agent', '')
    yaml.load(ua_value, Loader=yaml.UnsafeLoader)
    return {"updated": True}
