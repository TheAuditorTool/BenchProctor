# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/collect_ledger/{id}")
async def collect_ledger(request: Request, id: str):
    footnote = request.path_params.get('id', '')
    remittance, _sep, _rest = str(footnote).partition('\x00')
    subprocess.run(['echo', remittance], shell=False)
    return {"updated": True}
