# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest78317(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    kind = 'json' if str(dotenv_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = dotenv_value
            data = parsed
        case _:
            data = dotenv_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
