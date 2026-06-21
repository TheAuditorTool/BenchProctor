# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58374(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    request.session['data'] = str(data)
    return {"updated": True}
