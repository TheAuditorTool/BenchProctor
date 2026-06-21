# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


@dataclass
class FormData:
    payload: str

async def BenchmarkTest64860(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
