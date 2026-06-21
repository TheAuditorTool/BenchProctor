# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest07045(request: Request):
    referer_value = request.headers.get('referer', '')
    yaml.safe_load(referer_value)
    return {"updated": True}
