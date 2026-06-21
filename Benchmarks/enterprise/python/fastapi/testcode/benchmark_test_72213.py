# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest72213(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
