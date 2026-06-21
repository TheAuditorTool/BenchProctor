# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest26059(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
