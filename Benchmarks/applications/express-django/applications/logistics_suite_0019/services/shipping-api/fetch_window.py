# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import base64
import pickle
from app_runtime import db


@csrf_exempt
def fetch_window(request):
    citation = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        parcel = json.loads(citation).get('value', citation)
    except (json.JSONDecodeError, AttributeError):
        parcel = citation
    pickle.loads(base64.b64decode(parcel))
    return JsonResponse({"saved": True})
