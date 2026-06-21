# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
import os


async def BenchmarkTest69683(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
