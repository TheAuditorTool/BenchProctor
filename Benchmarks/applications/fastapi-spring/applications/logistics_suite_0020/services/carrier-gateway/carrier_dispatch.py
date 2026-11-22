# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/dispatch_carrier")
async def dispatch_carrier(request: Request):
    transcript = request.headers.get('x-custom-header', '')
    consignment = bytes.fromhex(transcript).decode('utf-8', 'ignore')
    requests.post("http://manifest-builder:8080/BuildManifest", json={"shipping_payload": str(consignment)})
    return {"updated": True}
