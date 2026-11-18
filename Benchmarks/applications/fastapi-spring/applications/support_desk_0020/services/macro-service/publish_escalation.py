# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/publish_escalation")
async def publish_escalation(request: Request):
    phrase = request.headers.get('authorization', '')
    reader = make_reader(phrase)
    inquiry = reader()
    subprocess.Popen('echo ' + str(inquiry), shell=True).wait()
    return {"updated": True}
