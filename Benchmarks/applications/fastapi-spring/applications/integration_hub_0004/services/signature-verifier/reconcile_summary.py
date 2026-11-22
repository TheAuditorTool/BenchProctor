# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/reconcile_summary")
async def reconcile_summary(request: Request):
    summary = request.headers.get('referer', '')
    reader = make_reader(summary)
    handshake = reader()
    subprocess.Popen('echo ' + str(handshake), shell=True).wait()
    return {"updated": True}
