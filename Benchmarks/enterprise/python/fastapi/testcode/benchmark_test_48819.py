# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest48819(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = str(secret_value).replace('\x00', '')
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
