# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest15849(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
