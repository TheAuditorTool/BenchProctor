# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest67223(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
