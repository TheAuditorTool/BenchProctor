# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
import ast


async def BenchmarkTest66932(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = str(ast.literal_eval(prop_value))
    except (ValueError, SyntaxError):
        data = prop_value
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return {"updated": True}
