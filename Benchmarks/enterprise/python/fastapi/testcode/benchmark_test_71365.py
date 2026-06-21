# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import ast


async def BenchmarkTest71365(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
