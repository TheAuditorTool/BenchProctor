# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/evaluate_rule")
async def evaluate_rule(request: Request):
    excerpt = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(excerpt).split(','):
        parts.append(token.strip())
    verdict = ','.join(parts)
    requests.post("http://watchlist-sync:8080/SyncWatchlist", json={"risk_payload": str(verdict)})
    return {"updated": True}
