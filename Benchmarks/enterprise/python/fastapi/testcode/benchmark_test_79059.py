# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest79059(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
