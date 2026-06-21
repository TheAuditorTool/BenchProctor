# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09606(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    int(str(data))
    return {"updated": True}
