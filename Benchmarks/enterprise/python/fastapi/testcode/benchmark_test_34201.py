# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest34201(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    os.system('echo ' + str(data))
    return {"updated": True}
