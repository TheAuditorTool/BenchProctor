# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest39518(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
