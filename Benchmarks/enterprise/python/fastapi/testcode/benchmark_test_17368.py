# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import os


async def BenchmarkTest17368(request: Request):
    secret_value = 'feature_flag_value'
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return {"updated": True}
