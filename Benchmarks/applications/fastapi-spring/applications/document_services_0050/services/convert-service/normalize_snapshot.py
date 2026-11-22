# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/normalize_snapshot")
async def normalize_snapshot(request: Request):
    citation = request.headers.get('authorization', '')
    parts = str(citation).split(',')
    dossier = ' '.join(parts)
    subprocess.Popen('echo ' + str(dossier), shell=True).wait()
    return {"updated": True}
