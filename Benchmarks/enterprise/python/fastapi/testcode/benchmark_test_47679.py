# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest47679(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    yaml.safe_load(data)
    return {"updated": True}
