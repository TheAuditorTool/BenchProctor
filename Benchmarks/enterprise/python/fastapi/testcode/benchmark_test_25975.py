# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25975(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    int(str(data))
    return {"updated": True}
