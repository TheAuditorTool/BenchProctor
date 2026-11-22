# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/reconcile_ticket/{id}")
async def reconcile_ticket(request: Request, id: str):
    remark = request.path_params.get('id', '')
    inquiry, _sep, _rest = str(remark).partition('\x00')
    subprocess.run(['echo', inquiry], shell=False)
    return {"updated": True}
