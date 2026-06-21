# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest73939(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
