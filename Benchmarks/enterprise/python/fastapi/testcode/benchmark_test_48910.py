# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest48910(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = f'{secret_value:.200s}'
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
