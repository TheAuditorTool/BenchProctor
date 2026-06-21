# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from dataclasses import dataclass
from starlette.responses import JSONResponse
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11085(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
