# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest45502(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
