# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/resolve_roster")
async def resolve_roster(request: Request):
    citation = (await request.body()).decode('utf-8')
    pending = list(str(citation).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    consignment = ','.join(collected)
    requests.get(str(consignment))
    return {"updated": True}
