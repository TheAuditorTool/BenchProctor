# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest63351(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
