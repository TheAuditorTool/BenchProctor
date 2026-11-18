# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/publish_config")
async def publish_config(request: Request):
    preface = request.headers.get('x-custom-header', '')
    remark = bytes.fromhex(preface).decode('utf-8', 'ignore')
    subprocess.run(['echo', remark], shell=False)
    return {"updated": True}
