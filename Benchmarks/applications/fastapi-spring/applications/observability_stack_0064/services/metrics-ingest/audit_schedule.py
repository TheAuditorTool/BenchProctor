# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/audit_schedule")
async def audit_schedule(request: Request):
    tagline = request.headers.get('referer', '')
    reader = make_reader(tagline)
    gauge = reader()
    subprocess.Popen('echo ' + str(gauge), shell=True).wait()
    return {"updated": True}
