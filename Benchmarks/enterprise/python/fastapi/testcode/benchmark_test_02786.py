# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02786(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    os.system('echo ' + str(data))
    return {"updated": True}
