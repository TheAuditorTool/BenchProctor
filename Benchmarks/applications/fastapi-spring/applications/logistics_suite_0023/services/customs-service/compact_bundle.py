# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/compact_bundle")
async def compact_bundle(request: Request):
    caption = request.headers.get('authorization', '')
    reader = make_reader(caption)
    parcel = reader()
    subprocess.Popen('echo ' + str(parcel), shell=True).wait()
    return {"updated": True}
