# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest73589(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = (lambda v: v.strip())(secret_value)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
