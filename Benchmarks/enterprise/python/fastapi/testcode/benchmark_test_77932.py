# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest77932(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return {"updated": True}
