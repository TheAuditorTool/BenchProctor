# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest74938(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
