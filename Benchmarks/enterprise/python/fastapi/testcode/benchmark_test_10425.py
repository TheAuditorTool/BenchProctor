# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest10425(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    requests.get(str(data))
    return {"updated": True}
