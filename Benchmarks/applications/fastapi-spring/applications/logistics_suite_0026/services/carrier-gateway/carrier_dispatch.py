# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/dispatch_carrier")
async def dispatch_carrier(request: Request):
    citation = request.query_params.get('id', '')
    parcel = (lambda v: v.strip())(citation)
    requests.post("http://manifest-builder:8080/BuildManifest", json={"shipping_payload": str(parcel)})
    return {"updated": True}
