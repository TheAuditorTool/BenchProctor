# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30465(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    eval(str(data))
    return {"updated": True}
