# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11603(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
