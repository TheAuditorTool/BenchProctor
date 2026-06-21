# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest76051(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    requests.get(str(data))
    return {"updated": True}
