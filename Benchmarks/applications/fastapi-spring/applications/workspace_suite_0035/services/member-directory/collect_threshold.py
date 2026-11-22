# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/collect_threshold/{id}")
async def collect_threshold(request: Request, id: str):
    paragraph = request.path_params.get('id', '')
    wording, _sep, _rest = str(paragraph).partition('\x00')
    subprocess.run(['echo', wording], shell=False)
    return {"updated": True}
