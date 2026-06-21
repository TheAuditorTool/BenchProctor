# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73816(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
