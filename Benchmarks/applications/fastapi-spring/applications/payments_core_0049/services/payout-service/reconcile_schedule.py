# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/reconcile_schedule/{id}")
async def reconcile_schedule(request: Request, id: str):
    headline = request.path_params.get('id', '')
    disbursement, _sep, _rest = str(headline).partition('\x00')
    subprocess.run(['echo', disbursement], shell=False)
    return {"updated": True}
