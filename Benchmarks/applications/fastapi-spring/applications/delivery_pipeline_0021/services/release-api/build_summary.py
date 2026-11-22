# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/build_summary/{id}")
async def build_summary(request: Request, id: str):
    summary = request.path_params.get('id', '')
    phrase, _sep, _rest = str(summary).partition('\x00')
    subprocess.run(['echo', phrase], shell=False)
    return {"updated": True}
