# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest11644(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = '%s' % str(secret_value)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
