# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05646(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
