# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import pickle


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06413(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
