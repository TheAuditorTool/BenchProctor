# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/compact_config/{id}")
async def compact_config(request: Request, id: str):
    footnote = request.path_params.get('id', '')
    addendum, _sep, _rest = str(footnote).partition('\x00')
    subprocess.run(['echo', addendum], shell=False)
    return {"updated": True}
