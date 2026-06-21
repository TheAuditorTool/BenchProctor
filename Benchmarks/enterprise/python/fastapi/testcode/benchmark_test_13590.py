# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from starlette.responses import HTMLResponse


async def BenchmarkTest13590(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
