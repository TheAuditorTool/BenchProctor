# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest21295(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    async def _evasion_task():
        requests.get(str(data))
    await _evasion_task()
    return {"updated": True}
