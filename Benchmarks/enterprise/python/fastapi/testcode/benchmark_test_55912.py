# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest55912(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    requests.get(str(data))
    return {"updated": True}
