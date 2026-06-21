# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest15011(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    requests.get(str(data))
    return {"updated": True}
