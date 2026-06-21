# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


async def BenchmarkTest09642(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    try:
        _bounded = int(data)
        if _bounded < 0 or _bounded > 10000:
            return JSONResponse({'error': 'out of range'}, status_code=400)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
