# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/audit_roster")
async def audit_roster(request: Request):
    memo = request.headers.get('authorization', '')
    reader = make_reader(memo)
    voucher = reader()
    subprocess.Popen('echo ' + str(voucher), shell=True).wait()
    return {"updated": True}
