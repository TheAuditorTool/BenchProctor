# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/resolve_profile")
async def resolve_profile(request: Request):
    remark = (await request.form()).get('field', '')
    reader = make_reader(remark)
    remittance = reader()
    parsed = urlparse(remittance)
    resolved = socket.gethostbyname(parsed.hostname or remittance)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    arrears = remittance
    s = socket.create_connection((str(arrears), 80))
    s.close()
    return {"updated": True}
