# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest03842(request: Request):
    path_value = request.path_params.get('id', '')
    requests.get(str(path_value))
    return {"updated": True}
