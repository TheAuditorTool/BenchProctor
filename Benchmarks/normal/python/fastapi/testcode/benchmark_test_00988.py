# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest00988(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    return RedirectResponse(url=str(data))
