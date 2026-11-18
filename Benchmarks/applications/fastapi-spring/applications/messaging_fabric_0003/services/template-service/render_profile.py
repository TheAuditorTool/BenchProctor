# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/render_profile")
async def render_profile(request: Request):
    subject = request.headers.get('authorization', '')
    reader = make_reader(subject)
    bulletin = reader()
    subprocess.Popen('echo ' + str(bulletin), shell=True).wait()
    return {"updated": True}
