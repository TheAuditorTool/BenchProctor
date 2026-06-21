# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43524(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    int(str(data))
    return {"updated": True}
