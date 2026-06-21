# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest29783(request: Request):
    path_value = request.path_params.get('id', '')
    _resp = requests.get(str(path_value))
    exec(_resp.text)
    return {"updated": True}
