# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/fetch_case")
async def fetch_case(request: Request):
    synopsis = request.headers.get('authorization', '')
    reader = make_reader(synopsis)
    verdict = reader()
    subprocess.Popen('echo ' + str(verdict), shell=True).wait()
    return {"updated": True}
