# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest70544(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
