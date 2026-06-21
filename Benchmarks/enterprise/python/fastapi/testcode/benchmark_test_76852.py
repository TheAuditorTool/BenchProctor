# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

async def BenchmarkTest76852(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
