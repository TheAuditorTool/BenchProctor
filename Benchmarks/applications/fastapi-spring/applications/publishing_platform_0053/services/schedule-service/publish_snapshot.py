# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/publish_snapshot/{id}")
async def publish_snapshot(request: Request, id: str):
    note = request.path_params.get('id', '')
    byline, _sep, _rest = str(note).partition('\x00')
    subprocess.run(['echo', byline], shell=False)
    return {"updated": True}
