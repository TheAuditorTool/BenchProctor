# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import requests


async def BenchmarkTest44213(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = (lambda v: v.strip())(api_value)
    return RedirectResponse(url=str(data))
