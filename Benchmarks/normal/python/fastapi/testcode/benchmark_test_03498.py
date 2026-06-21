# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def normalise_input(value):
    return value.strip()

async def BenchmarkTest03498(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    async def _evasion_task():
        requests.get(str(data))
    await _evasion_task()
    return {"updated": True}
