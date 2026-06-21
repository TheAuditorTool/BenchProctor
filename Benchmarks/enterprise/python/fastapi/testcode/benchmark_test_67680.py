# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

async def BenchmarkTest67680(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
