# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/enrich_window")
async def enrich_window(request: Request):
    caption = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(caption)
    subprocess.Popen('echo ' + str(consignment), shell=True).wait()
    return {"updated": True}
