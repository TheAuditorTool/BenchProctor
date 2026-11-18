# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/archive_policy")
async def archive_policy(request: Request):
    citation = request.headers.get('authorization', '')
    reader = make_reader(citation)
    backorder = reader()
    subprocess.Popen('echo ' + str(backorder), shell=True).wait()
    return {"updated": True}
