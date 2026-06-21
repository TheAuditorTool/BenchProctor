# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import pickle


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03854(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
