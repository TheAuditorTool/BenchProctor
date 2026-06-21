# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest18667(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    yaml.safe_load(data)
    return {"updated": True}
