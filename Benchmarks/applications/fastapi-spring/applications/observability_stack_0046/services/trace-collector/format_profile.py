# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/format_profile/{id}")
async def format_profile(request: Request, id: str):
    paragraph = request.path_params.get('id', '')
    gauge, _sep, _rest = str(paragraph).partition('\x00')
    subprocess.run(['echo', gauge], shell=False)
    return {"updated": True}
