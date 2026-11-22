# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/fetch_ticket/{id}")
async def fetch_ticket(request: Request, id: str):
    blurb = request.path_params.get('id', '')
    inquiry, _sep, _rest = str(blurb).partition('\x00')
    subprocess.run(['echo', inquiry], shell=False)
    return {"updated": True}
