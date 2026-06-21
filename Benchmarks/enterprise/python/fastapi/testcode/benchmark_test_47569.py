# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest47569(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = coalesce_blank(dotenv_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
