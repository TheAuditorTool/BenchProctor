# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/validate_receipt")
async def validate_receipt(request: Request):
    summary = request.headers.get('authorization', '')
    reader = make_reader(summary)
    gauge = reader()
    subprocess.Popen('echo ' + str(gauge), shell=True).wait()
    return {"updated": True}
