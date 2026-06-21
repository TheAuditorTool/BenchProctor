# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest16904(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    requests.get(str(data))
    return {"updated": True}
