# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11236(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    request.session['data'] = str(data)
    return {"updated": True}
