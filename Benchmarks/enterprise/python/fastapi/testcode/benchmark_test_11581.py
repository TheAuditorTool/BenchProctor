# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest11581(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
