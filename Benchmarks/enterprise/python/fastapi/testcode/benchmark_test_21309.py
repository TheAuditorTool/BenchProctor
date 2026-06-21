# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest21309(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    globals()['counter'] = int(data)
    return {"updated": True}
