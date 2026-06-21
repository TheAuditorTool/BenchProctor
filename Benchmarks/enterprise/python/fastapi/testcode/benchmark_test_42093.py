# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest42093(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
