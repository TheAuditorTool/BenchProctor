# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import json


async def BenchmarkTest56905(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    json.loads(data)
    return {"updated": True}
