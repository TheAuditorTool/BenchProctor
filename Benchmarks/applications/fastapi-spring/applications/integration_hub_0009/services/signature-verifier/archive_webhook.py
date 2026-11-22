# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/archive_webhook")
async def archive_webhook(request: Request):
    heading = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(heading)
    subprocess.Popen('echo ' + str(handshake), shell=True).wait()
    return {"updated": True}
