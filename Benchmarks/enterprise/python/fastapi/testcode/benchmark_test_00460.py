# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest00460(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(yaml_value)
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return {"updated": True}
