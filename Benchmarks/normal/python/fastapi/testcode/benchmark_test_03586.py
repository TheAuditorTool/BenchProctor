# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03586(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    yaml.safe_load(data)
    return {"updated": True}
