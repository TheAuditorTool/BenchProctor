# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53620(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    result = 100 / int(str(data))
    return {"updated": True}
