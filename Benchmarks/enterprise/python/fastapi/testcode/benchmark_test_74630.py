# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import os
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest74630(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
