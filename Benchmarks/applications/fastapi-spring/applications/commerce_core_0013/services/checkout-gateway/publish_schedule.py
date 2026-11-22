# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/publish_schedule")
async def publish_schedule(request: Request):
    wording = (await request.body()).decode('utf-8')
    reader = make_reader(wording)
    backorder = reader()
    subprocess.run('echo ' + str(backorder), shell=True)
    return {"updated": True}
