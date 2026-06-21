# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest73256(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
