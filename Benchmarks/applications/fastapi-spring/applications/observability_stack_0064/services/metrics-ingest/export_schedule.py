# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/export_schedule/{id}")
async def export_schedule(request: Request, id: str):
    tagline = request.path_params.get('id', '')
    gauge, _sep, _rest = str(tagline).partition('\x00')
    subprocess.run(['echo', gauge], shell=False)
    return {"updated": True}
