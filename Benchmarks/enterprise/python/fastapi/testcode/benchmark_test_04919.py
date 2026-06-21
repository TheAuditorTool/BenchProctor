# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


async def BenchmarkTest04919(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
