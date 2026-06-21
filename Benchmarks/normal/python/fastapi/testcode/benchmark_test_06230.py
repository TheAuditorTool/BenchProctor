# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06230(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
