# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/build_checkpoint/{id}")
async def build_checkpoint(request: Request, id: str):
    citation = request.path_params.get('id', '')
    dossier, _sep, _rest = str(citation).partition('\x00')
    subprocess.run(['echo', dossier], shell=False)
    return {"updated": True}
