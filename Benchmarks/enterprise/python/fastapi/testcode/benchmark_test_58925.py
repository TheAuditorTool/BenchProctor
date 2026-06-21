# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58925(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    exec(str(data))
    return {"updated": True}
