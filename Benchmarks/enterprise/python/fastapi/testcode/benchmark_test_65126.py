# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

async def BenchmarkTest65126(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
