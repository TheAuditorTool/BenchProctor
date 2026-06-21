# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
import ast
from Crypto.Cipher import AES


async def BenchmarkTest07528(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
