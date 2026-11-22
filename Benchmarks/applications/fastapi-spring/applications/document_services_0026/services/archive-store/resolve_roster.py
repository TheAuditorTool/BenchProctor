# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/resolve_roster/{id}")
async def resolve_roster(request: Request, id: str):
    preface = request.path_params.get('id', '')
    addendum, _sep, _rest = str(preface).partition('\x00')
    subprocess.run(['echo', addendum], shell=False)
    return {"updated": True}
