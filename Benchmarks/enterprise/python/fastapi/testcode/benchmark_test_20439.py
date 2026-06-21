# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest20439(request: Request):
    secret_value = 'app_display_name'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return {"updated": True}
