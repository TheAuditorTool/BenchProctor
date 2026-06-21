# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest17284(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    globals()['counter'] = int(data)
    return {"updated": True}
