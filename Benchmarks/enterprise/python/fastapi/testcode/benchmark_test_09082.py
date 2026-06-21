# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09082(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
