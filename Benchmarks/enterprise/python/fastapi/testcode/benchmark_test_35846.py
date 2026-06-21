# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest35846(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    requests.get(str(data))
    return {"updated": True}
