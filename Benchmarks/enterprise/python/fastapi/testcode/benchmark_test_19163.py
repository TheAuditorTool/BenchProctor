# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest19163(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    async def _evasion_task():
        requests.get(str(data))
    await _evasion_task()
    return {"updated": True}
