# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest43332(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    os.remove(str(data))
    return {"updated": True}
