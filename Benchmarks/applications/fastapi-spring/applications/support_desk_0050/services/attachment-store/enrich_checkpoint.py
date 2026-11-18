# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/enrich_checkpoint")
async def enrich_checkpoint(request: Request):
    remark = request.headers.get('authorization', '')
    reader = make_reader(remark)
    inquiry = reader()
    subprocess.Popen('echo ' + str(inquiry), shell=True).wait()
    return {"updated": True}
