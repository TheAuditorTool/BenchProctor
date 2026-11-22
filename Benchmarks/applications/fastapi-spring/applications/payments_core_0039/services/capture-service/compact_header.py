# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/compact_header")
async def compact_header(request: Request):
    memo = (await request.body()).decode('utf-8')
    reader = make_reader(memo)
    ledger = reader()
    subprocess.run('echo ' + str(ledger), shell=True)
    return {"updated": True}
