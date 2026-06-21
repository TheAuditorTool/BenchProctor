# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest03671(request: Request):
    secret_value = 'config_secret_test_abc123'
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
