# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import pickle


async def BenchmarkTest10317(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
