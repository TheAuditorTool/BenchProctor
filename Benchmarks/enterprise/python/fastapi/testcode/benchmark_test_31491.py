# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest31491(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
