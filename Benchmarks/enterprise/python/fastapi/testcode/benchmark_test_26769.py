# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


@dataclass
class FormData:
    payload: str

async def BenchmarkTest26769(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
