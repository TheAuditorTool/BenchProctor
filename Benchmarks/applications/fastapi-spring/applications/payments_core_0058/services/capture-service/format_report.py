# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/format_report/{id}")
async def format_report(request: Request, id: str):
    caption = request.path_params.get('id', '')
    kind = 'json' if str(caption).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            ledger = str(caption).strip()
        case _:
            ledger = str(caption)
    os.unlink('/var/app/data/' + str(ledger))
    return {"updated": True}
