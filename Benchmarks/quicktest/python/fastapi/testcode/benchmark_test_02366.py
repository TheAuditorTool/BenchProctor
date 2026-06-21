# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02366(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    yaml.safe_load(data)
    return {"updated": True}
