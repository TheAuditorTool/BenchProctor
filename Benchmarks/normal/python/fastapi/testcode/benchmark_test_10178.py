# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10178(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    eval(str(data))
    return {"updated": True}
