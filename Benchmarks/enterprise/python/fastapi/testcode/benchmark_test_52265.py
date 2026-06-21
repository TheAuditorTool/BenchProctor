# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest52265(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
