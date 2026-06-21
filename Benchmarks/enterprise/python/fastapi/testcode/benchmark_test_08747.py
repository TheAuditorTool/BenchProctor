# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest08747(request: Request):
    auth_header = request.headers.get('authorization', '')
    pickle.loads(auth_header.encode('latin-1'))
    return {"updated": True}
