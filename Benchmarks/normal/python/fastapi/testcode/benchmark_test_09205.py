# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest09205(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    if api_value:
        data = api_value
    else:
        data = ''
    requests.get(str(data))
    return {"updated": True}
