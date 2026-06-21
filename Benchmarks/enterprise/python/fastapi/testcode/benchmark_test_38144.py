# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

async def BenchmarkTest38144(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    importlib.import_module(str(data))
    return {"updated": True}
