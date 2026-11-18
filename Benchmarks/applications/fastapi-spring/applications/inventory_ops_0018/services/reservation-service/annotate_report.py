# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/annotate_report/{id}")
async def annotate_report(request: Request, id: str):
    transcript = request.path_params.get('id', '')
    kind = 'json' if str(transcript).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            backorder = str(transcript).strip()
        case _:
            backorder = str(transcript)
    os.unlink('/var/app/data/' + str(backorder))
    return {"updated": True}
