# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest31824(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
