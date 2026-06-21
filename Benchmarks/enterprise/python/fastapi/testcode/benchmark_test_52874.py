# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest52874(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
