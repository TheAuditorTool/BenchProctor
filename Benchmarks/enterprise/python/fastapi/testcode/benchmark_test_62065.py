# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest62065(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
