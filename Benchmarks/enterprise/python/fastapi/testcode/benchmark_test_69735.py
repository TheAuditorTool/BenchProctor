# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69735(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
