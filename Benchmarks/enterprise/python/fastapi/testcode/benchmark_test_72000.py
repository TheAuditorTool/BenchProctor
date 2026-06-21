# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest72000(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
