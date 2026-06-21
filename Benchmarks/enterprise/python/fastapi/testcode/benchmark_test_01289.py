# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest01289(request: Request, field: str = Form('')):
    field_value = field
    ciphertext = bytes(b ^ 0x42 for b in str(field_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
