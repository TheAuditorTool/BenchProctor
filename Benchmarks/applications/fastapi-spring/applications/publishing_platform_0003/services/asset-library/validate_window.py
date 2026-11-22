# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/validate_window")
async def validate_window(request: Request):
    heading = (await request.body()).decode('utf-8')
    reader = make_reader(heading)
    addendum = reader()
    subprocess.run('echo ' + str(addendum), shell=True)
    return {"updated": True}
