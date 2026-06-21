# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest65308(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = '%s' % str(secret_value)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
