# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest12949(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
