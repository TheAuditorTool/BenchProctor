# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest10808(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    requests.get(str(data))
    return {"updated": True}
