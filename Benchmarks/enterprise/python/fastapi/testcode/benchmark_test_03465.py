# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import pickle


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03465(request: Request):
    referer_value = request.headers.get('referer', '')
    data = FormData(payload=referer_value).payload
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
