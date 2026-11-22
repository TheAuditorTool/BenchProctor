# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/fetch_checkpoint")
async def fetch_checkpoint(request: Request):
    wording = (await request.body()).decode('utf-8')
    reader = make_reader(wording)
    consignment = reader()
    subprocess.run('echo ' + str(consignment), shell=True)
    return {"updated": True}
