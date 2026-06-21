# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest46567(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
