# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import requests
import ast


async def BenchmarkTest06642(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    try:
        data = str(ast.literal_eval(api_value))
    except (ValueError, SyntaxError):
        data = api_value
    async def _evasion_task():
        return RedirectResponse(url=str(data))
    return await _evasion_task()
