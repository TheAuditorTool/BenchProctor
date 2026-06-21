# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest18058(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    os.system('echo ' + str(data))
    return {"updated": True}
